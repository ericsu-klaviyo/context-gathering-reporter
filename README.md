Context Gathering Reporter
===
This repository contains a collection of scripts to aid in the summarization of i18 context gathering reports. This was originally made for Flows teams and certain features are hard-coded for Flows' purposes.

The `reports/2024-04-02` directory has been included for examplification, otherwise other report directories and files are not committed to the repository.

# Usage
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

For Flows, to report all of today's reports (assuming they've been downloaded and named appropriately):
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
...etc
```