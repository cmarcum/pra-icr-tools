# pra-icr-tools
Python scripts to help collect Paperwork Reduction Act Information Collections documents and metadata from reginfo.gov.

This repository contains Python tools designed to query, scrape, and download metadata and documents associated with information collection requests from the Office of Management and Budget's (OMB) Office of Information and Regulatory Affairs (OIRA) Paperwork Reduction Act (PRA) database [reginfo.gov](https://reginfo.gov). 

## Background

I wrote these scripts to support research, policy analysis, and the evaluation of federal data integrity by extracting comprehensive historical inventories and raw agency documents.

The reginfo.gov has an old, outdated techstack that is largely supported by a single individual in OIRA. It currently lacks a public-facing API and the site instead relies on deeply nested and often malformed HTML tables, fragile session states, hidden anti-forgery tokens, and document downloads that are obscured behind specific JavaScript triggers rather than standard URL hyperlinks. Because basic web scraping methods routinely fail against these structural idiosyncrasies extracting comprehensive historical inventories requires a custom-built approach. The tools developed here bypass these hurdles by programmatically intercepting and passing hidden form tokens to preserve state during complex pagination and utilizing a hybrid Document-Object Model (DOM) and regex to identify and retrieve files hidden behind legacy frontend code.

Currently, there are two python scripts in this repository:
* pra-icr-search.py creates a way to automagically pull search results from querying [PRASearch](https://www.reginfo.gov/public/do/PRASearch)
* pra-icr-download.py downloads documents from the ICR records pages in a reasonable file structure
More details about each tool are provided below.

Several code-blocks were generated using Google's gemini (I've indicated in the script comments where that's the case). 

## Prerequisites
Ensure you have Python 3.7+ installed. Dependicies (mainly, [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for access to it's great DOM handlers), are located in [requirements.txt](requirements.txt), which can be installed:
```bash
pip install -r requirements.txt
```

---

## Tool 1: PRA ICR Search (`pra-icr-search.py`)

### Description
A command-line headless scraper that maps directly to the RegInfo PRASearch form at [https://www.reginfo.gov/public/do/PRASearch](https://www.reginfo.gov/public/do/PRASearch). It automatically handles form tokens, complex pagination (including hybrid JavaScript triggers), and features a "Reactive Chunker" to work around the 1000 response limit that is hard-coded into reginfo.gov. If reginfo.gov rejects a query for exceeding its 1,000-result limit, the script intercepts the failure and automatically slices massive, multi-year queries into safe monthly blocks. 

It also features graceful interruption: pressing `Ctrl+C` will halt the scrape and securely save all data collected up to that exact moment.

Because the PRASearch relies on codes to indicate which agency or type of ICR (for example) as internal query elements, you should reference the [codebook](codebook.md) for help in writing search queries with this tool.

### Output
A single CSV file containing the tabular metadata for the requested Information Collection Requests (ICRs). Fields include: 


|`OMB Control No` | `Agency/Sub` | `Title` | `Request Type` | `Date Received` | `Concluded Date` | `Conclusion Action` | `Current Expiration Date` | `No. of ICs` | `No. of Forms`|
|-|-|-|-|-|-|-|-|-|-|

### Example Use Cases

**1. Track Federal Data Disconinuations**
Extract every single form that was discontinued government-wide during 2025. If this exceeds 1,000 records, the script will automatically chunk the timeline.
```bash
python pra-icr-search.py dateType=DI startDate=01/01/2025 endDate=12/31/2025 --output 2025_disruptions.csv --delay 2
```

**2. Evaluate Agency ICR activity over a fixed time period**
Pull a comprehensive history of the Environmental Protection Agency's concluded ICRs over a four-year span.
```bash
python pra-icr-search.py agencyCode=2000 dateType=CO startDate=01/01/2021 endDate=12/31/2024 --output epa_4_year_history.csv --delay 2
```

**3. Agency Active Inventory**
Pull all currently active forms for the IRS. This bypasses the chunker and leverages the bulletproof pagination handler to walk through dozens of pages.
```bash
python pra-icr-search.py agencyCode=1500 subAgencyCode=1545 icrStatus=AC --output irs_active_forms.csv --delay 2
```

**4. Track Emerging Collections**
Identify brand new forms (not extensions or revisions) currently sitting at OIRA awaiting initial approval.
```bash
python pra-icr-search.py icrStatus=RE requestType=RN --output new_collections_pending.csv --delay 2
```

---

## Tool 2: PRA ICR Downloader (`pra-icr-download.py`)

### Description
A document crawler that takes a specific ICR Reference Number and downloads all attached physical files (including collection instruments, subparts A and B, public comments, and more). Because agencies nest their actual surveys and forms deep within the site structure, this script automatically hunts for and traverses "child" subpages for Information Collection pages. 

It extracts native filenames from reginfo's `Content-Disposition` headers. If the server fails to provide a name, it dynamically infers the correct file extension based on the MIME type. The script also takes into account the fact that agencies are allowed to upload redundantly named files and handles file-name collisions by auto-incrementing duplicate filenames to ensure no redundant agency uploads are overwritten.

### Output
The script generates a parent directory named after the target ICR Reference Number. Depending on the command-line flags provided, it builds strictly named subdirectories (`Collection_Instruments` and/or `Supporting_Documents`) inside the parent folder, populated with the raw files (PDFs, Word docs, Excel sheets, etc.).

### Example Use Cases

**1. Download Everything (Collections and Supporting Documents)**
This example uses a recent CDC collection:
```bash
python pra-icr-download.py 202601-0920-012 --both
```

*Expected Output Structure:*
```text
202601-0920-012/
├── Collection_Instruments/
│   ├── Att_B_NOFO_DMP_20260113_FINAL_VERSION.pdf
│   └── ...
└── Supporting_Documents/
    ├── 30-Day_FRN_SSA_Data_Management_Plan_(DMP)_Template.docx
    └── ...
```

**2. Download Only the Collection Instruments**
```bash
python pra-icr-download.py 202601-0920-012 --collections
```

**3. Download Only Supporting Documents**
```bash
python pra-icr-download.py 202601-0920-012 --supporting
```

---

For both functions, please ensure the `--delay` parameter is used responsibly to avoid overwhelming federal servers during large, automated queries.
