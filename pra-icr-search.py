'''
This script provides full PRAsearch capability from the command-line using python.
 The script should automagically detect when the 1000 limit would be 
 hit had then chunck by month and resume. If that fails, well...IDK.
 
You can gracefully exit this script using ctrl+c

Some code-blocks were generated using Google Gemini (as indicated in the comments).
 
Last updated: 2.27.2026
   
'''
import argparse
import requests
from bs4 import BeautifulSoup
import sys
import time
import csv
import urllib.parse
import re
from datetime import datetime, timedelta
import calendar

BASE_URL = "https://www.reginfo.gov"
SEARCH_URL = f"{BASE_URL}/public/do/PRASearch"

EXPECTED_HEADERS = [
    "OMB Control No", "Agency/Sub", "Title", "Request Type", 
    "Date Received", "Concluded Date", "Conclusion Action", 
    "Current Expiration Date", "No. of ICs", "No. of Forms"
]

def parse_args():
    parser = argparse.ArgumentParser(description="Exact-mapped reactive scraper for RegInfo PRA Search.")
    parser.add_argument('fields', nargs='*', help="Search fields as key=value pairs matching the HTML form")
    parser.add_argument('--output', default="pra_results.csv", help="Output CSV filename")
    parser.add_argument('--delay', type=int, default=2, help="Delay between page requests")
    return parser.parse_args()

def get_monthly_chunks(start_str, end_str):
    try:
        start_date = datetime.strptime(start_str, "%m/%d/%Y")
        end_date = datetime.strptime(end_str, "%m/%d/%Y")
    except ValueError:
        print("[!] Date format error. Ensure dates are strictly MM/DD/YYYY.")
        sys.exit(1)

    chunks = []
    current_start = start_date

    while current_start <= end_date:
        last_day = calendar.monthrange(current_start.year, current_start.month)[1]
        current_end = datetime(current_start.year, current_start.month, last_day)
        if current_end > end_date:
            current_end = end_date
        chunks.append((current_start.strftime("%m/%d/%Y"), current_end.strftime("%m/%d/%Y")))
        current_start = current_end + timedelta(days=1)
        
    return chunks

def scrape_payload(session, user_params, delay):
    """
    This massive code chunk was written with Google gemini. It executes the search using the 
    forms and r eturns a status flag and the extracted rows.
    """
    try:
        initial_resp = session.get(SEARCH_URL, timeout=15)
        soup = BeautifulSoup(initial_resp.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"  [!] Initial handshake failed: {e}")
        return "ERROR", []

    payload = {}
    form = soup.find('form', id='PRASearchForm')
    if form:
        for hidden in form.find_all('input', type='hidden'):
            name = hidden.get('name')
            value = hidden.get('value', '')
            if name:
                payload[name] = value

    payload['operation'] = '2'
    payload.update(user_params)
    
    post_headers = session.headers.copy()
    post_headers['Content-Type'] = 'application/x-www-form-urlencoded'
    
    try:
        response = session.post(SEARCH_URL, data=payload, headers=post_headers, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  [!] Error on search POST request: {e}")
        return "ERROR", []

    page_number = 1
    extracted_rows = []
    
    try:
        while True:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if page_number == 1:
                limit_warning = soup.find(string=re.compile(r'allowed maximum number of results is 1000', re.IGNORECASE))
                if limit_warning:
                    return "LIMIT_EXCEEDED", []
                page_text = soup.get_text(separator=' ')
                records_match = re.search(r'Number Of Records Found:\s*([\d,]+)', page_text, re.IGNORECASE)
                if records_match:
                    print(f"  [*] Total Records Found: {records_match.group(1)}")
                else:
                    print("  [*] Total Records Found: (Could not parse number from page)")

            target_table = None
            for th in soup.find_all(['th', 'td']):
                if "OMB Control No" in th.get_text(strip=True):
                    target_table = th.find_parent('table')
                    break
            
            if not target_table:
                tables = soup.find_all('table')
                if tables:
                    target_table = max(tables, key=lambda t: len(t.find_all('tr')))

            if not target_table:
                if page_number > 1:
                    print(f"  [-] Next page loaded successfully, but no data table was found. Ending pagination.")
                break
                
            rows_added_this_page = 0
            for row in target_table.find_all('tr'):
                cols = [col.get_text(strip=True) for col in row.find_all(['td', 'th'], recursive=False)]
                if len(cols) >= 9:
                    if "OMB Control No" in cols[0] or "OMB Control No" in cols[1]:
                        continue 
                    extracted_rows.append(cols[:10])
                    rows_added_this_page += 1
                    
            print(f"  [*] Scraped page {page_number}. Rows collected: {rows_added_this_page} (Total: {len(extracted_rows)})")
                    
            if rows_added_this_page == 0 and page_number > 1:
                print("  [-] Next page loaded but contained no data rows. Ending pagination.")
                break
                
            next_href = None
            for a in soup.find_all('a'):
                if not a.has_attr('href'):
                    continue
                text = a.get_text(strip=True).lower()
                alt_texts = " ".join([img.get('alt', '').lower() for img in a.find_all('img')])
                if 'next' in text or '>>' in text or 'next' in alt_texts:
                    next_href = a['href']
                    break
                    
            if not next_href:
                match = re.search(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(?:[^<]*?(?:next|&gt;&gt;|>>)[^<]*?)</a>', response.text, re.IGNORECASE)
                if match:
                    next_href = match.group(1)
                    print("  [*] (Next link was found using Regex Fallback)")
            
            if next_href:
                print(f"  [*] Navigating to next link: {next_href}")
                
                if 'javascript:' in next_href.lower() or next_href == '#':
                    onclick = soup.find('a', href=next_href).get('onclick', '') if soup.find('a', href=next_href) else ''
                    match = re.search(r'(\d+)', next_href + onclick)
                    if match:
                        next_page_num = match.group(1)
                        payload['page_number'] = next_page_num
                        page_number += 1
                        time.sleep(delay)
                        try:
                            response = session.post(SEARCH_URL, data=payload, headers=post_headers, timeout=15)
                            response.raise_for_status()
                        except requests.exceptions.RequestException as e:
                            print(f"  [!] Error fetching POST page {page_number}: {e}")
                            break
                    else:
                        break
                else:
                    next_url = urllib.parse.urljoin(SEARCH_URL, next_href)
                    current_form = soup.find('form', id='PRASearchForm')
                    fresh_payload = {}
                    if current_form:
                        for hidden in current_form.find_all('input', type='hidden'):
                            if hidden.get('name'):
                                fresh_payload[hidden.get('name')] = hidden.get('value', '')
                    fresh_payload['operation'] = '2'
                    fresh_payload.update(user_params)
                    
                    page_number += 1
                    time.sleep(delay)
                    try:
                        session.headers.update({'Referer': response.url})
                        response = session.get(next_url, params=fresh_payload, timeout=15) 
                        response.raise_for_status()
                    except requests.exceptions.RequestException as e:
                        print(f"  [!] Error fetching GET page {page_number}: {e}")
                        break
            else:
                print("  [*] No 'Next' link detected. Reached the end of the results.")
                break
    # I needed a graceful way of stopping this behemoth; just using ctrl+c            
    except KeyboardInterrupt:
        return "INTERRUPTED", extracted_rows

    if len(extracted_rows) > 0:
        return "SUCCESS", extracted_rows
    else:
        return "NO JOY", []


def main():
    args = parse_args()
    
    user_params = {}
    for field in args.fields:
        if '=' in field:
            key, val = field.split('=', 1)
            user_params[key] = val
        else:
            print(f"[!] Warning: Ignoring invalid field '{field}'. Use key=value.")

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Origin': BASE_URL,
        'Referer': SEARCH_URL
    })
    
    all_master_results = [EXPECTED_HEADERS]

    try:
        print(f"[*] Attempting primary search: {user_params}")
        status, extracted_data = scrape_payload(session, user_params, args.delay)

        if status == "LIMIT_EXCEEDED":
            print("[!] You've angered OIRA: The query hit the 1000 database limit.")
            
            if 'startDate' in user_params and 'endDate' in user_params:
                print("[*] Mike Johnson can't stop you now: Automatically slicing query into monthly chunks...")
                date_chunks = get_monthly_chunks(user_params['startDate'], user_params['endDate'])
                
                for i, (chunk_start, chunk_end) in enumerate(date_chunks, 1):
                    print(f"\n[*] Processing Chunk {i}/{len(date_chunks)}: {chunk_start} to {chunk_end}")
                    chunk_params = user_params.copy()
                    chunk_params['startDate'] = chunk_start
                    chunk_params['endDate'] = chunk_end
                    
                    if i > 1:
                        time.sleep(args.delay)
                        
                    chunk_status, chunk_data = scrape_payload(session, chunk_params, args.delay)
                    
                    all_master_results.extend(chunk_data)

                    if chunk_status == "INTERRUPTED":
                        raise KeyboardInterrupt
                    elif chunk_status == "LIMIT_EXCEEDED":
                         print(f"  [!] WARNING: This specific month exceeded 1000 records. Data truncated and you may need to further limit the dates manually.")
                    elif chunk_status == "SUCCESS":
                         print(f"  [+] Finalized Chunk {i}. Total chunk records: {len(chunk_data)}")
                    else:
                         print("  [-] No records found for this month.")
            else:
                print("[!] Cannot auto-chunk because 'startDate' and 'endDate' were not provided.")
                print("[!] You must narrow your search criteria manually.")
                
        else:
            all_master_results.extend(extracted_data)
            if status == "INTERRUPTED":
                raise KeyboardInterrupt
            elif status == "SUCCESS":
                print(f"  [+] Search completed normally. Extracted {len(extracted_data)} total records.")
            else:
                 print("[-] No records found for your query.")

    except KeyboardInterrupt:
        print("\n\n[!] Script manually interrupted by user (Ctrl+C)!")
        print("[!] Halting the scraper and saving the data collected so far...")

    total_records = len(all_master_results) - 1
    if total_records > 0:
        print(f"[*] Writing {total_records} TOTAL records to {args.output}...")
        with open(args.output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(all_master_results)
        print("[*] Complete.")
    else:
        print("[-] CSV file was not created because no data were collected.")

if __name__ == "__main__":
    main()
