Context Gathering Reporter
===
This repository contains a collection of scripts to aid in the summarization of i18 context gathering reports. This was originally made for Flows teams and certain features are hard-coded for Flows' purposes.

The `reports/2024-04-02` directory has been included for examplification, otherwise other report directories and files are not committed to the repository.

# Setup
Make sure to install repository requirements with
```
pip install -r requirements.txt
```

For "Today's Stats", context gathering reports are expected to be downloaded and named in the following manner in the repository's directory:
```
reports/
-- YYYY-MM-DD/
    -- teamname.json
```

For Flows teams, this looks like the following for April 2nd, 2024:
```
reports/
-- 2024-04-01/
    -- flims.json
    -- interface.json
    -- platform.json
```

# Usage
## Single Report File
To get the report of a single report file:
```
> python report_parser.py reports/2024-04-02/platform.json

Domain                        # Missing    %
--------------------------  -----------  ---
flows-debug-tools                     1   5%
flows-evaluations-activity           83  85%
web-feeds                            10  26%
--------------------------  -----------  ---
```

## Today's Reports (Flows only)


For Flows, to summarize all of today's reports (assuming they've been downloaded and named appropriately):
```
> python todays_stats.py --summary

2024-04-02

Domain       # Missing    %
---------  -----------  ---
Interface         1209  47%
FLIMS              546  53%
Platform            94  60%
```

For Flows, to report all of today's reports:
```
> python todays_stats.py

2024-04-02

-  -  -  -  -  -  -  -  -
I  n  t  e  r  f  a  c  e
-  -  -  -  -  -  -  -  -
Domain                                    # Missing    %
--------------------------------------  -----------  ---
ab-navigation-experiment                          1  50%
account-menu                                      1   2%
...
tags                                             15  48%
--------------------------------------  -----------  ---
Total                                          1209  47%


-  -  -  -  -
F  L  I  M  S
-  -  -  -  -
Domain                            # Missing    %
------------------------------  -----------  ---
export-analytics                          7  23%
filter-builder                          273  68%
...
staff-flows-audit                         9   1%
------------------------------  -----------  ---
Total                                   546  53%


-  -  -  -  -  -  -  -
P  l  a  t  f  o  r  m
-  -  -  -  -  -  -  -
Domain                        # Missing    %
--------------------------  -----------  ---
flows-debug-tools                     1   5%
flows-evaluations-activity           83  85%
web-feeds                            10  26%
--------------------------  -----------  ---
Total                                94  60%
```