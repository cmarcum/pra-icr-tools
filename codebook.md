# PRA ICR Search Codebook

This codebook contains all the index codes mapping to the various parameters available on the RegInfo.gov Paperwork Reduction Act (PRA) Information Collection Review search form available at: [https://www.reginfo.gov/public/do/PRASearch](https://www.reginfo.gov/public/do/PRASearch). 

These codes can be passed directly as parameters to the `pra-icr-search.py` script.

## 1. ICR Function Index Codes

### Request Type (`requestType`)
| Code | Description |
| :--- | :--- |
| `EX` | Extension without change of a currently approved collection |
| `EC` | Existing collection in use without an OMB Control Number |
| `RW` | Reinstatement with change of a previously approved collection |
| `RN` | New collection (Request for a new OMB Control Number) |
| `CH` | No material or nonsubstantive change to a currently approved collection |
| `RV` | Revision of a currently approved collection |
| `RO` | Reinstatement without change of a previously approved collection |
| `CR` | RCF Recertification |
| `CC` | RCF No material or nonsubstantive change to a currently approved collection |
| `CN` | RCF New |

### Date Type (`dateType`)
| Code | Description |
| :--- | :--- |
| `RE` | Received |
| `CO` | Concluded |
| `AC` | Act By |
| `EX` | Expired |
| `DI` | Discontinued |
| `EI` | Expiring |

### ICR Status (`icrStatus`)
| Code | Description |
| :--- | :--- |
| `AC` | Active |
| `RE` | Received in OIRA |
| `HI` | Historical Inactive |
| `HA` | Historical Active |
| `PA` | PreApproved |

### Conclusion Action (`conclusionCode`)
| Code | Description |
| :--- | :--- |
| `CI` | Comment filed on Interim Final Rule |
| `CN` | Comment filed on Interim Final Rule and continue |
| `DA` | Disapproved |
| `AW` | Approved without change |
| `AC` | Approved with change |
| `CP` | Comment filed on proposed rule |
| `PA` | Preapproved |
| `WD` | Withdrawn |
| `WC` | Withdrawn and continue |
| `NP` | Not subject to PRA |
| `NC` | Not subject to PRA and continue |
| `IS` | Improperly submitted |
| `IC` | Improperly submitted and continue |
| `DE` | Delegated |
| `CC` | Comment filed on proposed rule and continue |
| `DC` | Disapproved and continue |
| `RI` | Returned - Improperly Submitted |
| `RR` | Returned to Agency for Reconsideration |
| `RO` | Returned - Outside Generic Clearance |
| `AP` | Approved |

### Type of Review (`reviewType`)
| Code | Description |
| :--- | :--- |
| `RE` | Regular |
| `EM` | Emergency |
| `DE` | Delegated |

### Certification (`certification`)
| Code | Description |
| :--- | :--- |
| `1` | (a) It is necessary for the proper performance of agency functions |
| `2` | (b) It avoids unnecessary duplication |
| `3` | (c) It reduces burden on small entities |
| `4` | (d) It uses plain, coherent, and unambiguous language...... |
| `5` | (e) Its implementation will be consistent and compatible...... |
| `6` | (f) It indicates the retention periods for recordkeeping requirements |
| `7` | (g) It informs respondents of the information called for...... |
| `8` | (h) It was developed by an office that has planned and allocated...... |
| `9` | (i) It uses effective and efficient statistical survey methodology...... |
| `10` | (j) It makes appropriate use of information technology |

### ICR Ended Due To (`icrDueTo`)
| Code | Description |
| :--- | :--- |
| `DC` | Discontinued |
| `DN` | Disapproved and Not Continued |
| `EX` | Expired |
| `NA` | New Approval |
| `TD` | Transfer ended OMB Ctl No. |

### Obligation to Respond (`obligation`)
| Code | Description |
| :--- | :--- |
| `MA` | Mandatory |
| `RO` | Required to Obtain or Retain Benefits |
| `VO` | Voluntary |

### Burden Due To (`burdenDueTo`)
| Code | Description |
| :--- | :--- |
| `RP` | Reporting |
| `RK` | Record Keeping |
| `TD` | Third Party Disclosure |
| `PK` | Reporting and Record Keeping |
| `PT` | Reporting and Third Party Disclosure |
| `KT` | Record Keeping and Third Party Disclosure |
| `AL` | All Three Types |

### Affected Public (`affectPublic`)
| Code | Description |
| :--- | :--- |
| `BP` | Businesses or other for-profits |
| `FA` | Farms |
| `FG` | Federal Government |
| `IH` | Individuals or Households |
| `NP` | Not-for-profit institutions |
| `PS` | Private Sector |
| `SL` | State, Local, and Tribal Governments |

### ICRs That (`otherCondition`)
| Code | Description |
| :--- | :--- |
| `0` | Are generic |
| `1` | Privacy impact assessment |
| `2` | Are preapproved |
| `3` | Affect small entities |
| `4` | Received public comments |
| `5` | Relate to proposed rulemaking |
| `6` | Employ statistical methods |
| `7` | Relate to interim/final rulemaking |
| `8` | Sponsor common form(s) |
| `9` | Include form(s) |
| `10` | Include collections available electronically |
| `11` | Include collections that can be submitted electronically |
| `12` | Relate to other documents for OIRA review |
| `13` | Relate to the Affordable Care Act [Pub. L. 111-148 & 111-152] |
| `14` | Relate to the Dodd-Frank Wall Street Reform and Consumer Protection Act, [Pub. L. 111-203] |
| `15` | Relate to the American Recovery and Reinvestment Act of 2009 (ARRA) |
| `16` | Request any personally identifiable information [OMB Circular No. A-130] |
| `17` | Include a form that requires a Privacy Act Statement [5 U.S.C. §552a(e)(3)] |
| `18` | Relate to the Pandemic Response |

## 2. Federal Agency & Sub-Agency Index Codes

Use the **Agency Code** for the `agencyCode` parameter, and the **Sub-Agency Code** for the `subAgencyCode` parameter.

| Agency / Sub-Agency Name | Agency Code (`agencyCode`) | Sub-Agency Code (`subAgencyCode`) |
| :--- | :--- | :--- |
| **ACTION** | `3001` | |
| **Administration for Strategic Preparedness and Response** | `3065` | |
| **Administrative Conference of the United States** | `3002` | |
| **Advisory Council on Historic Preservation** | `3010` | |
| **African Development Foundation** | `3005` | |
| **Agency for International Development** | `0412` | |
| **All** | `0000` | |
| **American Battle Monuments Commission** | `3263` | |
| **Appalachian Regional Commission** | `3011` | |
| **Appraisal Subcommittee of the FFIEC** | `3139` | |
| **Architectural and Transportation Barriers Compliance Board** | `3014` | |
| **Armed Forces Retirement Home** | `3030` | |
| **Barry M. Goldwater Scholarship and Excellence in Education Foundation** | `3019` | |
| **Board of Directors of the HOPE for Homeowners Program** | `2580` | |
| **Civil Aeronautics Board** | `3024` | |
| **Committee for Purchase From People Who Are Blind or Severely Disabled** | `3037` | |
| **Commodity Futures Trading Commission** | `3038` | |
| **Community Services Administration [INACTIVATED 1981]** | `3039` | |
| **Consumer Financial Protection Bureau** | `3170` | |
| **Consumer Product Safety Commission** | `3041` | |
| **Continuity of Operations** | `0375` | |
| **Corporation for National and Community Service** | `3045` | |
| **Council of the Inspectors General on Integrity and Efficiency** | `3219` | |
| **Council on Environmental Quality** | `0331` | |
| **Council on Wage and Price Stability [INACTIVE 1981]** | `0334` | |
| **Court Services and Offender Supervision Agency for the District of Columbia** | `3225` | |
| **DMS** | `0005` | |
| **DOD/GSA/NASA (FAR)** | `9000` | |
| **Defense Nuclear Facilities Safety Board** | `3155` | |
| **Delta Regional Authority** | `4718` | |
| **Denali Commission** | `9572` | |
| **Department of Agriculture** | `0500` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `0500` | `0503` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Inspector General | `0500` | `0504` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Chief Financial Officer | `0500` | `0505` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Communications | `0500` | `0506` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Transportation | `0500` | `0507` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Civil Rights | `0500` | `0508` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Homeland Security | `0500` | `0509` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the General Counsel | `0500` | `0510` |
| &nbsp;&nbsp;&nbsp;&nbsp;Client Technology Services | `0500` | `0517` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agricultural Research Service | `0500` | `0518` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Institute of Food and Agriculture | `0500` | `0524` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Grants and Program Systems | `0500` | `0525` |
| &nbsp;&nbsp;&nbsp;&nbsp;Extension Service | `0500` | `0527` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Agricultural Library | `0500` | `0530` |
| &nbsp;&nbsp;&nbsp;&nbsp;Science and Education | `0500` | `0531` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Agricultural Statistical Service | `0500` | `0535` |
| &nbsp;&nbsp;&nbsp;&nbsp;Economic Research Service | `0500` | `0536` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agricultural Cooperative Service | `0500` | `0537` |
| &nbsp;&nbsp;&nbsp;&nbsp;World Agricultural Outlook Board | `0500` | `0550` |
| &nbsp;&nbsp;&nbsp;&nbsp;Foreign Agricultural Service | `0500` | `0551` |
| &nbsp;&nbsp;&nbsp;&nbsp;Foreign Assistance Programs | `0500` | `0557` |
| &nbsp;&nbsp;&nbsp;&nbsp;Farm Service Agency | `0500` | `0560` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Crop Insurance Corporation | `0500` | `0563` |
| &nbsp;&nbsp;&nbsp;&nbsp;Farm Production and Conservation Business Center | `0500` | `0565` |
| &nbsp;&nbsp;&nbsp;&nbsp;Commodity Credit Corporation | `0500` | `0566` |
| &nbsp;&nbsp;&nbsp;&nbsp;Rural Business-Cooperative Service | `0500` | `0570` |
| &nbsp;&nbsp;&nbsp;&nbsp;Rural Utilities Service | `0500` | `0572` |
| &nbsp;&nbsp;&nbsp;&nbsp;Rural Housing Service | `0500` | `0575` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Rural Development Policy | `0500` | `0576` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of International Cooperation & Development | `0500` | `0577` |
| &nbsp;&nbsp;&nbsp;&nbsp;Natural Resources Conservation Service | `0500` | `0578` |
| &nbsp;&nbsp;&nbsp;&nbsp;Animal and Plant Health Inspection Service | `0500` | `0579` |
| &nbsp;&nbsp;&nbsp;&nbsp;Grain Inspection, Packers and Stockyards Administration | `0500` | `0580` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agricultural Marketing Service | `0500` | `0581` |
| &nbsp;&nbsp;&nbsp;&nbsp;Food Safety and Inspection Service | `0500` | `0583` |
| &nbsp;&nbsp;&nbsp;&nbsp;Food and Nutrition Service | `0500` | `0584` |
| &nbsp;&nbsp;&nbsp;&nbsp;Human Nutrition Information Service | `0500` | `0586` |
| &nbsp;&nbsp;&nbsp;&nbsp;Packers and Stockyards Administration | `0500` | `0590` |
| &nbsp;&nbsp;&nbsp;&nbsp;Forest Service | `0500` | `0596` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Energy | `0500` | `0598` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Contracting and Procurement | `0500` | `0599` |
| **Department of Commerce** | `0600` | |
| &nbsp;&nbsp;&nbsp;&nbsp;General Administration | `0600` | `0605` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of the Census | `0600` | `0607` |
| &nbsp;&nbsp;&nbsp;&nbsp;Economic and Statistical Analysis | `0600` | `0608` |
| &nbsp;&nbsp;&nbsp;&nbsp;Economic Development Administration | `0600` | `0610` |
| &nbsp;&nbsp;&nbsp;&nbsp;International Trade Administration | `0600` | `0625` |
| &nbsp;&nbsp;&nbsp;&nbsp;Minority Business Development Agency | `0600` | `0640` |
| &nbsp;&nbsp;&nbsp;&nbsp;United States Travel and Tourism Administration | `0600` | `0644` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Oceanic and Atmospheric Administration | `0600` | `0648` |
| &nbsp;&nbsp;&nbsp;&nbsp;Patent and Trademark Office | `0600` | `0651` |
| &nbsp;&nbsp;&nbsp;&nbsp;Science and Technical Research | `0600` | `0652` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Telecommunications and Information Administration | `0600` | `0660` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `0600` | `0690` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Economic Analysis | `0600` | `0691` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Technical Information Service | `0600` | `0692` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Institute of Standards and Technology | `0600` | `0693` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Industry and Security | `0600` | `0694` |
| **Department of Defense** | `0700` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Department of the Air Force | `0700` | `0701` |
| &nbsp;&nbsp;&nbsp;&nbsp;Department of the Army | `0700` | `0702` |
| &nbsp;&nbsp;&nbsp;&nbsp;Department of the Navy | `0700` | `0703` |
| &nbsp;&nbsp;&nbsp;&nbsp;Departmental and Others | `0700` | `0704` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Under Secretary of Defense for Intelligence | `0700` | `0705` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Army Corps of Engineers | `0700` | `0710` |
| &nbsp;&nbsp;&nbsp;&nbsp;US Marine Corps | `0700` | `0712` |
| &nbsp;&nbsp;&nbsp;&nbsp;Space Force | `0700` | `0715` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Assistant Secretary for Health Affairs | `0700` | `0720` |
| &nbsp;&nbsp;&nbsp;&nbsp;Defense Finance and Accounting Service | `0700` | `0730` |
| &nbsp;&nbsp;&nbsp;&nbsp;Defense Acquisition Regulations Council | `0700` | `0750` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `0700` | `0790` |
| **Department of Education** | `1800` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the General Counsel | `1800` | `1801` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Elementary and Secondary Education | `1800` | `1810` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Special Education and Rehabilitative Services | `1800` | `1820` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Career, Technical, and Adult Education | `1800` | `1830` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Postsecondary Education | `1800` | `1840` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Federal Student Aid | `1800` | `1845` |
| &nbsp;&nbsp;&nbsp;&nbsp;Institute of Education Sciences | `1800` | `1850` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Innovation and Improvement | `1800` | `1855` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Communications and Outreach | `1800` | `1860` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Safe and Drug-Free Schools | `1800` | `1865` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office for Civil Rights | `1800` | `1870` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Planning, Evaluation and Policy Development | `1800` | `1875` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Management | `1800` | `1880` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of English Language Acquistion | `1800` | `1885` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Chief Financial Officer | `1800` | `1890` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Chief Information Officer | `1800` | `1891` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Inspector General | `1800` | `1892` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Institute for Literacy | `1800` | `1893` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `1800` | `1894` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Under Secretary | `1800` | `1895` |
| **Department of Energy** | `1900` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Departmental and Others | `1900` | `1901` |
| &nbsp;&nbsp;&nbsp;&nbsp;Economic Regulatory Administration | `1900` | `1903` |
| &nbsp;&nbsp;&nbsp;&nbsp;Energy Efficiency and Renewable Energy | `1900` | `1904` |
| &nbsp;&nbsp;&nbsp;&nbsp;Energy Information Administration | `1900` | `1905` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Administration | `1900` | `1910` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Chief Financial Officer | `1900` | `1920` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of State and Community Energy Programs | `1900` | `1930` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of General Counsel | `1900` | `1990` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Acquisition Management | `1900` | `1991` |
| &nbsp;&nbsp;&nbsp;&nbsp;Defense and Security Affairs | `1900` | `1992` |
| &nbsp;&nbsp;&nbsp;&nbsp;Policy, Safety, and Environment | `1900` | `1993` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Nuclear Security Administration | `1900` | `1994` |
| **Department of Health and Human Services** | `0900` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Public Health Service | `0900` | `0905` |
| &nbsp;&nbsp;&nbsp;&nbsp;Health Resources and Services Administration | `0900` | `0906` |
| &nbsp;&nbsp;&nbsp;&nbsp;Program Support Center | `0900` | `0907` |
| &nbsp;&nbsp;&nbsp;&nbsp;Administration for Strategic Preparedness and Response | `0900` | `0908` |
| &nbsp;&nbsp;&nbsp;&nbsp;Food and Drug Administration | `0900` | `0910` |
| &nbsp;&nbsp;&nbsp;&nbsp;Health Services Administration | `0900` | `0915` |
| &nbsp;&nbsp;&nbsp;&nbsp;Indian Health Service | `0900` | `0917` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agency for Healthcare Research and Quality | `0900` | `0919` |
| &nbsp;&nbsp;&nbsp;&nbsp;Centers for Disease Control and Prevention | `0900` | `0920` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agency for Toxic Substances and Disease Registry | `0900` | `0923` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Institutes of Health | `0900` | `0925` |
| &nbsp;&nbsp;&nbsp;&nbsp;Substance Abuse and Mental Health Services Administration | `0900` | `0930` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agency for Healthcare Research and Quality | `0900` | `0935` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Inspector General | `0900` | `0936` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Assistant Secretary for Health | `0900` | `0937` |
| &nbsp;&nbsp;&nbsp;&nbsp;Centers for Medicare & Medicaid Services | `0900` | `0938` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Public Health and Science | `0900` | `0940` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office for Civil Rights | `0900` | `0945` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Consumer Information and Insurance Oversight | `0900` | `0950` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the National Coordinator for Health Information Technology | `0900` | `0955` |
| &nbsp;&nbsp;&nbsp;&nbsp;Administration for Children and Families | `0900` | `0970` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Human Development Services | `0900` | `0980` |
| &nbsp;&nbsp;&nbsp;&nbsp;Administration for Community Living | `0900` | `0985` |
| &nbsp;&nbsp;&nbsp;&nbsp;Departmental Management | `0900` | `0990` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `0900` | `0991` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Family Assistance | `0900` | `0992` |
| **Department of Homeland Security** | `1600` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `1600` | `1601` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Civil Rights | `1600` | `1610` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Citizenship and Immigration Services | `1600` | `1615` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Secret Service | `1600` | `1620` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Coast Guard | `1600` | `1625` |
| &nbsp;&nbsp;&nbsp;&nbsp;Directorate of Information and Analysis and Infrastructure Protection | `1600` | `1630` |
| &nbsp;&nbsp;&nbsp;&nbsp;Directorate of Science and Technology | `1600` | `1640` |
| &nbsp;&nbsp;&nbsp;&nbsp;Homeland Security Advanced Research Projects Agency | `1600` | `1641` |
| &nbsp;&nbsp;&nbsp;&nbsp;Directorate of Border and Transportation Security | `1600` | `1650` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Customs and Border Protection | `1600` | `1651` |
| &nbsp;&nbsp;&nbsp;&nbsp;Transportation Security Administration | `1600` | `1652` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Immigration and Customs Enforcement | `1600` | `1653` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Emergency Management Agency | `1600` | `1660` |
| &nbsp;&nbsp;&nbsp;&nbsp;Cybersecurity and Infrastructure Security Agency | `1600` | `1670` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Undersecretary for Management | `1600` | `1680` |
| &nbsp;&nbsp;&nbsp;&nbsp;Customs Revenue Functions | `1600` | `1685` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Inspector General | `1600` | `1690` |
| **Department of Housing and Urban Development** | `2500` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `2500` | `2501` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Housing | `2500` | `2502` |
| &nbsp;&nbsp;&nbsp;&nbsp;Government National Mortgage Association | `2500` | `2503` |
| &nbsp;&nbsp;&nbsp;&nbsp;Solar Energy and Energy Conservation Bank | `2500` | `2504` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Multifamily Assistance Restructuring | `2500` | `2505` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Community Planning and Development | `2500` | `2506` |
| &nbsp;&nbsp;&nbsp;&nbsp;Real Estate Assessment Center | `2500` | `2507` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Inspector General | `2500` | `2508` |
| &nbsp;&nbsp;&nbsp;&nbsp;Enforcement Center | `2500` | `2509` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the General Counsel | `2500` | `2510` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Chief Financial Officer | `2500` | `2511` |
| &nbsp;&nbsp;&nbsp;&nbsp;New Communities Development Corporation | `2500` | `2512` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Chief Information Officer | `2500` | `2513` |
| &nbsp;&nbsp;&nbsp;&nbsp;Policy Development and Research | `2500` | `2528` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Fair Housing and Equal Opportunity | `2500` | `2529` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Administration | `2500` | `2535` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Lead-Based Paint and Poison Prevention | `2500` | `2539` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Public and Indian Housing | `2500` | `2577` |
| **Department of Justice** | `1100` | |
| &nbsp;&nbsp;&nbsp;&nbsp;General Administration | `1100` | `1103` |
| &nbsp;&nbsp;&nbsp;&nbsp;United States Parole Commission | `1100` | `1104` |
| &nbsp;&nbsp;&nbsp;&nbsp;Legal Activities | `1100` | `1105` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Bureau of Investigation | `1100` | `1110` |
| &nbsp;&nbsp;&nbsp;&nbsp;Immigration and Naturalization Service | `1100` | `1115` |
| &nbsp;&nbsp;&nbsp;&nbsp;Drug Enforcement Administration | `1100` | `1117` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Prisons | `1100` | `1120` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Justice Programs | `1100` | `1121` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of  Violence Against Women | `1100` | `1122` |
| &nbsp;&nbsp;&nbsp;&nbsp;Criminal Division | `1100` | `1123` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Security Division | `1100` | `1124` |
| &nbsp;&nbsp;&nbsp;&nbsp;Executive Office for Immigration Review | `1100` | `1125` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Alcohol, Tobacco, Firearms, and Explosives | `1100` | `1140` |
| &nbsp;&nbsp;&nbsp;&nbsp;Civil Rights Division | `1100` | `1190` |
| **Department of Labor** | `1200` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Employment and Training Administration | `1200` | `1205` |
| &nbsp;&nbsp;&nbsp;&nbsp;Employee Benefits Security Administration | `1200` | `1210` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the American Workplace/Office of Labor Management Standards | `1200` | `1214` |
| &nbsp;&nbsp;&nbsp;&nbsp;Employment Standards Administration | `1200` | `1215` |
| &nbsp;&nbsp;&nbsp;&nbsp;Occupational Safety and Health Administration | `1200` | `1218` |
| &nbsp;&nbsp;&nbsp;&nbsp;Mine Safety and Health Administration | `1200` | `1219` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Labor Statistics | `1200` | `1220` |
| &nbsp;&nbsp;&nbsp;&nbsp;Departmental Management | `1200` | `1225` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Disability Employment Policy | `1200` | `1230` |
| &nbsp;&nbsp;&nbsp;&nbsp;Wage and Hour Division | `1200` | `1235` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Workers' Compensation Programs | `1200` | `1240` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Labor-Management Standards | `1200` | `1245` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Federal Contract Compliance Programs | `1200` | `1250` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `1200` | `1290` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Assistant Secretary for Administration and Management | `1200` | `1291` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Inspector General | `1200` | `1292` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Assistant Secretary for Veterans' Employment and Training | `1200` | `1293` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the American Workplace | `1200` | `1294` |
| **Department of State** | `1400` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Administration of Foreign Affairs | `1400` | `1405` |
| **Department of Transportation** | `2100` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `2100` | `2105` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary - Aviation | `2100` | `2106` |
| &nbsp;&nbsp;&nbsp;&nbsp;Transportation Security Administration | `2100` | `2110` |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Coast Guard | `2100` | `2115` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Aviation Administration | `2100` | `2120` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Highway Administration | `2100` | `2125` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Motor Carrier Safety Administration | `2100` | `2126` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Highway Traffic Safety Administration | `2100` | `2127` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Railroad Administration | `2100` | `2130` |
| &nbsp;&nbsp;&nbsp;&nbsp;Federal Transit Administration | `2100` | `2132` |
| &nbsp;&nbsp;&nbsp;&nbsp;Maritime Administration | `2100` | `2133` |
| &nbsp;&nbsp;&nbsp;&nbsp;Saint Lawrence Seaway Development Corporation | `2100` | `2135` |
| &nbsp;&nbsp;&nbsp;&nbsp;Pipeline and Hazardous Materials Safety Administration | `2100` | `2137` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Transportation Statistics - Aviation | `2100` | `2138` |
| &nbsp;&nbsp;&nbsp;&nbsp;Research and Innovative Technologies Administration | `2100` | `2139` |
| &nbsp;&nbsp;&nbsp;&nbsp;Pipeline and Hazardous Materials Safety Administration | `2100` | `2145` |
| &nbsp;&nbsp;&nbsp;&nbsp;Research and Innovative Technologies Administration (Old) | `2100` | `2150` |
| **Department of Veterans Affairs** | `2900` | |
| **Department of the Interior** | `1000` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Land Management | `1000` | `1004` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Reclamation | `1000` | `1006` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Water Policy | `1000` | `1008` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Ocean Energy Management | `1000` | `1010` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Natural Resources Revenue | `1000` | `1012` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Safety and Environmental Enforcement | `1000` | `1014` |
| &nbsp;&nbsp;&nbsp;&nbsp;United States Fish and Wildlife Service | `1000` | `1018` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Park Service | `1000` | `1024` |
| &nbsp;&nbsp;&nbsp;&nbsp;Geological Survey | `1000` | `1028` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Surface Mining Reclamation and Enforcement | `1000` | `1029` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Mines | `1000` | `1032` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Trust Funds Administration | `1000` | `1035` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Planning and Performance Management | `1000` | `1040` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Indian Affairs | `1000` | `1076` |
| &nbsp;&nbsp;&nbsp;&nbsp;Assistant Secretary for Land and Minerals Management | `1000` | `1082` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Acquisition and Property Management | `1000` | `1084` |
| &nbsp;&nbsp;&nbsp;&nbsp;Indian Arts and Crafts Board | `1000` | `1085` |
| &nbsp;&nbsp;&nbsp;&nbsp;National Biological Service | `1000` | `1089` |
| &nbsp;&nbsp;&nbsp;&nbsp;Assistant Secretary for Policy, Management and Budget | `1000` | `1090` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office for Equal Opportunity | `1000` | `1091` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Solicitor | `1000` | `1092` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Secretary | `1000` | `1093` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Hearings and Appeals | `1000` | `1094` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Inspector General | `1000` | `1095` |
| **Department of the Treasury** | `1500` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Departmental Offices | `1500` | `1505` |
| &nbsp;&nbsp;&nbsp;&nbsp;Financial Crimes Enforcement Network | `1500` | `1506` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Revenue Sharing | `1500` | `1507` |
| &nbsp;&nbsp;&nbsp;&nbsp;Financial Management Service | `1500` | `1510` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Alcohol, Tobacco and Firearms | `1500` | `1512` |
| &nbsp;&nbsp;&nbsp;&nbsp;Alcohol and Tobacco Tax and Trade Bureau | `1500` | `1513` |
| &nbsp;&nbsp;&nbsp;&nbsp;Customs Revenue Function | `1500` | `1515` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of Engraving and Printing | `1500` | `1520` |
| &nbsp;&nbsp;&nbsp;&nbsp;United States Mint | `1500` | `1525` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of the Fiscal Service | `1500` | `1530` |
| &nbsp;&nbsp;&nbsp;&nbsp;Bureau of the Public Debt | `1500` | `1535` |
| &nbsp;&nbsp;&nbsp;&nbsp;Internal Revenue Service | `1500` | `1545` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Thrift Supervision | `1500` | `1550` |
| &nbsp;&nbsp;&nbsp;&nbsp;Thrift Depositor Protection Oversight Board [TRANSFERRED TO 1505 in 1996] | `1500` | `1551` |
| &nbsp;&nbsp;&nbsp;&nbsp;United States Secret Service | `1500` | `1555` |
| &nbsp;&nbsp;&nbsp;&nbsp;Comptroller of the Currency | `1500` | `1557` |
| &nbsp;&nbsp;&nbsp;&nbsp;Community Development Financial Institutions Fund | `1500` | `1559` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the General Counsel | `1500` | `1590` |
| &nbsp;&nbsp;&nbsp;&nbsp;Treasury Inspector General for Tax Administration | `1500` | `1591` |
| **EEI Communications** | `5555` | |
| **Emergency Guarantee Loan Board** | `3047` | |
| **Emergency Oil and Gas Guaranteed Loan Board** | `3003` | |
| **Emergency Steel Guarantee Loan Board** | `3004` | |
| **Environmental Protection Agency** | `2000` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Boston | `2000` | `2001` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office New York | `2000` | `2002` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Philadelphia | `2000` | `2003` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Atlanta | `2000` | `2004` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Chicago | `2000` | `2005` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Dallas | `2000` | `2006` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Kansas City | `2000` | `2007` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Denver | `2000` | `2008` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office San Francisco | `2000` | `2009` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Policy | `2000` | `2010` |
| &nbsp;&nbsp;&nbsp;&nbsp;Regional Office Seattle | `2000` | `2012` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of General Counsel | `2000` | `2015` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Enforcement and Compliance Assurance | `2000` | `2020` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Environmental Information | `2000` | `2025` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Mission Support | `2000` | `2030` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Environmental Justice and External Civil Rights | `2000` | `2035` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Water | `2000` | `2040` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of International and Tribal Affairs | `2000` | `2045` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Land and Emergency Management | `2000` | `2050` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Office of the Chief Financial Officer | `2000` | `2055` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Air and Radiation | `2000` | `2060` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Inspector General | `2000` | `2065` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Chemical Safety and Pollution Prevention | `2000` | `2070` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of Research and Development | `2000` | `2080` |
| &nbsp;&nbsp;&nbsp;&nbsp;Office of the Administrator | `2000` | `2090` |
| **Equal Employment Opportunity Commission** | `3046` | |
| **Executive Office of the President** | `0300` | |
| **Export-Import Bank of the United States** | `3048` | |
| **Extra prefix from existing RMS OMB_NBR** | `7101` | |
| **Extra prefix from existing RMS OMB_NBR** | `5505` | |
| **Extra prefix from existing RMS OMB_NBR** | `3131` | |
| **Farm Credit Administration** | `3052` | |
| **Farm Credit System Assistance Board** | `3053` | |
| **Farm Credit System Insurance Corporation** | `3055` | |
| **Federal Communications Commission** | `3060` | |
| **Federal Council on the Arts and the Humanities** | `3134` | |
| **Federal Deposit Insurance Corporation** | `3064` | |
| **Federal Emergency Management Agency** | `3067` | |
| **Federal Energy Regulatory Commission** | `1902` | |
| **Federal Home Loan Bank Board** | `3068` | |
| **Federal Housing Finance Agency** | `2590` | |
| **Federal Housing Finance Board** | `3069` | |
| **Federal Labor Relations Authority** | `3070` | |
| **Federal Maritime Commission** | `3072` | |
| **Federal Mediation and Conciliation Service** | `3076` | |
| **Federal Mine Safety and Health Review Commission** | `3079` | |
| **Federal Permitting Improvement Steering Council** | `3121` | |
| **Federal Reserve System** | `7100` | |
| **Federal Trade Commission** | `3084` | |
| **Financial Stability Oversight Council** | `4030` | |
| **Foundation for Education Assistance** | `3086` | |
| **General Services Administration** | `3090` | |
| **Governmentwide Forms and Regulations** | `9999` | |
| **Grants.gov** | `4040` | |
| **Gulf Coast Ecosystem Restoration Council** | `3600` | |
| **Harry S Truman Scholarship Foundation** | `3111` | |
| **Index Cross References** | `0001` | |
| **Institute of Museum and Library Services** | `3137` | |
| **Inter-American Foundation** | `0417` | |
| **Interagency Council on the Homeless** | `3114` | |
| **International Boundary and Water Commission** | `1410` | |
| **International Trade Commission** | `3117` | |
| **Interstate Commerce Commission** | `3120` | |
| **James Madison Memorial Fellowship Foundation** | `3020` | |
| **Joint Board for The Enrollment of Actuaries** | `3410` | |
| **Legal Services Corporation** | `3122` | |
| **Library of Congress** | `3470` | |
| &nbsp;&nbsp;&nbsp;&nbsp;U.S. Copyright Office | `3470` | `3471` |
| **Merit Systems Protection Board** | `3124` | |
| **Military Compensation and Retirement Modernization Commission** | `3260` | |
| **Millennium Challenge Corporation** | `0414` | |
| **Morris K. Udall and Stewart L. Udall Foundation** | `3320` | |
| **National Aeronautics and Space Administration** | `2700` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Kennedy Space Center | `2700` | `2730` |
| **National Archives and Records Administration** | `3095` | |
| **National Assessment Governing Board** | `3098` | |
| **National Capital Planning Commission** | `3125` | |
| **National Commission on Libraries and Information Science** | `3130` | |
| **National Commission on Military, National, and Public Service** | `3262` | |
| **National Council on Disability** | `3480` | |
| **National Credit Union Administration** | `3133` | |
| **National Endowment for the Arts** | `3135` | |
| **National Endowment for the Humanities** | `3136` | |
| **National Gallery of Art** | `3100` | |
| **National Indian Gaming Commission** | `3141` | |
| **National Institute for Literacy** | `3430` | |
| **National Institute of Building Sciences** | `3138` | |
| **National Labor Relations Board** | `3142` | |
| **National Mediation Board** | `3140` | |
| **National Science Foundation** | `3145` | |
| **National Transportation Safety Board** | `3147` | |
| **Nuclear Regulatory Commission** | `3150` | |
| **Occupational Safety and Health Review Commission** | `3202` | |
| **Office of Director of National Intelligence** | `3440` | |
| **Office of Federal Housing Enterprise Oversight** | `2550` | |
| **Office of Government Ethics** | `3209` | |
| **Office of Historical Trust Accounting** | `1050` | |
| **Office of Management and Budget** | `0348` | |
| **Office of National Drug Control Policy** | `3201` | |
| **Office of Navajo and Hopi Indian Relocation** | `3148` | |
| **Office of Personnel Management** | `3206` | |
| **Office of Science and Technology Policy** | `0349` | |
| **Office of Special Counsel** | `3255` | |
| **Office of the Federal Coordinator for Alaska Natural Gas Transportation Projects** | `3080` | |
| **Office of the Federal Inspector, Alaska Natural Gas Transportation System** | `3204` | |
| **Office of the Intellectual Property Enforcement Coordinator** | `0355` | |
| **Office of the National Cyber Director** | `0301` | |
| **Office of the United States Trade Representative** | `0350` | |
| **Other Independent Agencies** | `3200` | |
| **Other Temporary Commissions** | `3312` | |
| **Overseas Private Investment Corporation** | `3420` | |
| **Panama Canal Commission** | `3207` | |
| **Peace Corps** | `0420` | |
| **Pennsylvania Avenue Development Corporation** | `3208` | |
| **Pension Benefit Guaranty Corporation** | `1212` | |
| **Postal Regulatory Commission** | `3211` | |
| **Presidio Trust** | `3212` | |
| **Privacy and Civil Liberties Oversight Board** | `0311` | |
| **Railroad Retirement Board** | `3220` | |
| **Recovery Accountability and Transparency Board** | `0430` | |
| **Regulatory Program Overviews** | `0002` | |
| **Resolution Trust Corporation** | `3205` | |
| **Securities and Exchange Commission** | `3235` | |
| **Selective Service System** | `3240` | |
| **Small Business Administration** | `3245` | |
| **Smithsonian Institution** | `3250` | |
| **Social Security Administration** | `0960` | |
| **Special Inspector General for Afghanistan Reconstruction** | `3460` | |
| **Special Inspector General for Iraq Reconstruction** | `3450` | |
| **Surface Transportation Board** | `2140` | |
| **TEST** | `0592` | |
| **Tennessee Valley Authority** | `3316` | |
| **The White House Office** | `0310` | |
| **Thrift Depositor Protection Oversight Board** | `3203` | |
| **U.S. Agency for Global Media** | `3112` | |
| **U.S. Chemical Safety and Hazard Investigation Board** | `3301` | |
| **U.S. Commission on Civil Rights** | `3035` | |
| **U.S. Election Assistance Commission** | `3265` | |
| **U.S. Government Publishing Office** | `3700` | |
| **U.S. Trade and Development Agency** | `3330` | |
| **United States Information Agency** | `3116` | |
| **United States International Development Finance Corporation** | `3015` | |
| **United States Metric Board** | `3327` | |
| **United States Postal Service** | `3210` | |
| &nbsp;&nbsp;&nbsp;&nbsp;United States Postal Inspection Service | `3210` | `3213` |
| **Vietnam Education Foundation** | `3085` | |
| **Water Resources Council [INACTIVATED 1982]** | `3335` | |

## 3. Line of Business & Subfunction Index Codes

Use the **Line of Business Code** for the `lineOfBusiness` parameter, and the **Subfunction Code** for the `subfunction` parameter.

| Line of Business / Subfunction Name | Line of Business Code (`lineOfBusiness`) | Subfunction Code (`subfunction`) |
| :--- | :--- | :--- |
| **Community and Social Services** | `101` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Homeownership Promotion | `101` | `001` |
| &nbsp;&nbsp;&nbsp;&nbsp;Community and Regional Development | `101` | `002` |
| &nbsp;&nbsp;&nbsp;&nbsp;Social Services | `101` | `003` |
| &nbsp;&nbsp;&nbsp;&nbsp;Postal Service | `101` | `004` |
| **Correctional Activities** | `102` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Criminal Incarceration | `102` | `005` |
| &nbsp;&nbsp;&nbsp;&nbsp;Criminal Rehabilitation | `102` | `006` |
| **Defense and National Security** | `103` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Strategic National and Theater Defense | `103` | `210` |
| &nbsp;&nbsp;&nbsp;&nbsp;Operational Defense | `103` | `211` |
| &nbsp;&nbsp;&nbsp;&nbsp;Tactical Defense | `103` | `212` |
| **Disaster Management** | `104` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Disaster Monitoring and Prediction | `104` | `007` |
| &nbsp;&nbsp;&nbsp;&nbsp;Disaster Preparedness and Planning | `104` | `008` |
| &nbsp;&nbsp;&nbsp;&nbsp;Disaster Repair and Restore | `104` | `009` |
| &nbsp;&nbsp;&nbsp;&nbsp;Emergency Response | `104` | `010` |
| **Economic Development** | `105` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Business and Industry Development | `105` | `011` |
| &nbsp;&nbsp;&nbsp;&nbsp;Intellectual Property Protection | `105` | `012` |
| &nbsp;&nbsp;&nbsp;&nbsp;Financial Sector Oversight | `105` | `013` |
| &nbsp;&nbsp;&nbsp;&nbsp;Industry Sector Income Stabilization  | `105` | `014` |
| **Education** | `106` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Elementary, Secondary, and Vocational Education | `106` | `015` |
| &nbsp;&nbsp;&nbsp;&nbsp;Higher Education | `106` | `016` |
| &nbsp;&nbsp;&nbsp;&nbsp;Cultural and Historic Preservation | `106` | `017` |
| &nbsp;&nbsp;&nbsp;&nbsp;Cultural and Historic Exhibition | `106` | `018` |
| **Energy** | `107` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Energy Supply | `107` | `019` |
| &nbsp;&nbsp;&nbsp;&nbsp;Energy Conservation and Preparedness | `107` | `020` |
| &nbsp;&nbsp;&nbsp;&nbsp;Energy Resource Management | `107` | `021` |
| &nbsp;&nbsp;&nbsp;&nbsp;Energy Production | `107` | `022` |
| **Environmental Management** | `108` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Environmental Monitoring and Forecasting | `108` | `023` |
| &nbsp;&nbsp;&nbsp;&nbsp;Environmental Remediation | `108` | `024` |
| &nbsp;&nbsp;&nbsp;&nbsp;Pollution Prevention and Control | `108` | `025` |
| **General Government** | `315` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Central Fiscal Operations | `315` | `175` |
| &nbsp;&nbsp;&nbsp;&nbsp;Legislative Functions | `315` | `176` |
| &nbsp;&nbsp;&nbsp;&nbsp;Executive Functions | `315` | `177` |
| &nbsp;&nbsp;&nbsp;&nbsp;Central Property Management | `315` | `178` |
| &nbsp;&nbsp;&nbsp;&nbsp;Central Personnel | `315` | `179` |
| &nbsp;&nbsp;&nbsp;&nbsp;Taxation Management | `315` | `180` |
| &nbsp;&nbsp;&nbsp;&nbsp;Central Records & Statistical Mgt | `315` | `181` |
| **General Science and Innovation** | `109` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Scientific and Technological Research and Innovation  | `109` | `026` |
| &nbsp;&nbsp;&nbsp;&nbsp;Space Exploration and Innovation | `109` | `027` |
| **Health** | `110` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Illness Prevention | `110` | `028` |
| &nbsp;&nbsp;&nbsp;&nbsp;Immunization Management | `110` | `029` |
| &nbsp;&nbsp;&nbsp;&nbsp;Public Health Monitoring | `110` | `030` |
| &nbsp;&nbsp;&nbsp;&nbsp;Health Care Services | `110` | `031` |
| &nbsp;&nbsp;&nbsp;&nbsp;Consumer Health and Safety | `110` | `032` |
| **Homeland Security** | `111` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Border and Transportation Security | `111` | `033` |
| &nbsp;&nbsp;&nbsp;&nbsp;Key Asset and Critical Infrastructure Protection | `111` | `034` |
| &nbsp;&nbsp;&nbsp;&nbsp;Catastrophic Defense | `111` | `035` |
| **Income Security** | `112` | |
| &nbsp;&nbsp;&nbsp;&nbsp;General Retirement and Disability | `112` | `036` |
| &nbsp;&nbsp;&nbsp;&nbsp;Unemployment Compensation | `112` | `037` |
| &nbsp;&nbsp;&nbsp;&nbsp;Housing Assistance | `112` | `038` |
| &nbsp;&nbsp;&nbsp;&nbsp;Food and Nutrition Assistance | `112` | `039` |
| &nbsp;&nbsp;&nbsp;&nbsp;Survivor Compensation | `112` | `040` |
| **Intelligence Operations** | `113` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Intelligence Planning and Direction/Needs | `113` | `213` |
| &nbsp;&nbsp;&nbsp;&nbsp;Intelligence Collection | `113` | `214` |
| &nbsp;&nbsp;&nbsp;&nbsp;Intelligence Analysis and Production | `113` | `215` |
| &nbsp;&nbsp;&nbsp;&nbsp;Dissemination | `113` | `216` |
| **International Affairs and Commerce** | `114` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Foreign Affairs | `114` | `041` |
| &nbsp;&nbsp;&nbsp;&nbsp;International Development and Humanitarian Aid | `114` | `042` |
| &nbsp;&nbsp;&nbsp;&nbsp;Global Trade | `114` | `043` |
| **Law Enforcement** | `115` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Criminal Apprehension | `115` | `044` |
| &nbsp;&nbsp;&nbsp;&nbsp;Criminal Investigation and Surveillance | `115` | `045` |
| &nbsp;&nbsp;&nbsp;&nbsp;Citizen Protection | `115` | `046` |
| &nbsp;&nbsp;&nbsp;&nbsp;Crime Prevention | `115` | `047` |
| &nbsp;&nbsp;&nbsp;&nbsp;Leadership Protection | `115` | `048` |
| &nbsp;&nbsp;&nbsp;&nbsp;Property Protection | `115` | `049` |
| &nbsp;&nbsp;&nbsp;&nbsp;Substance Control | `115` | `050` |
| **Litigation and Judicial Activities** | `116` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Judicial Hearing | `116` | `051` |
| &nbsp;&nbsp;&nbsp;&nbsp;Legal Defense | `116` | `052` |
| &nbsp;&nbsp;&nbsp;&nbsp;Legal Investigation | `116` | `053` |
| &nbsp;&nbsp;&nbsp;&nbsp;Legal Prosecution and Litigation | `116` | `054` |
| &nbsp;&nbsp;&nbsp;&nbsp;Resolution Facilitation | `116` | `055` |
| **Natural Resources** | `117` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Water Resource Management | `117` | `056` |
| &nbsp;&nbsp;&nbsp;&nbsp;Conservation, Marine and Land Management | `117` | `057` |
| &nbsp;&nbsp;&nbsp;&nbsp;Recreational Resource Management and Tourism | `117` | `058` |
| &nbsp;&nbsp;&nbsp;&nbsp;Agricultural Innovation and Services | `117` | `059` |
| **Supply Chain Management** | `405` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Goods Acquisition | `405` | `143` |
| &nbsp;&nbsp;&nbsp;&nbsp;Inventory Control | `405` | `144` |
| &nbsp;&nbsp;&nbsp;&nbsp;Logistics Management | `405` | `145` |
| &nbsp;&nbsp;&nbsp;&nbsp;Services Acquisition | `405` | `146` |
| **Transportation** | `118` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Air Transportation | `118` | `060` |
| &nbsp;&nbsp;&nbsp;&nbsp;Ground Transportation | `118` | `061` |
| &nbsp;&nbsp;&nbsp;&nbsp;Water Transportation | `118` | `062` |
| &nbsp;&nbsp;&nbsp;&nbsp;Space Operations | `118` | `063` |
| **Workforce Management** | `119` | |
| &nbsp;&nbsp;&nbsp;&nbsp;Training and Employment | `119` | `064` |
| &nbsp;&nbsp;&nbsp;&nbsp;Labor Rights Management | `119` | `065` |
| &nbsp;&nbsp;&nbsp;&nbsp;Worker Safety | `119` | `066` |
