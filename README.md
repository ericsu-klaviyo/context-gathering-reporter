Context Gathering Reporter
This repository contains a collection of scripts to aid in the summarization of i18n context gathering reports. This was originally made for Flows teams and certain features may contain Flows remnants.
===

The `reports/2024-04-02` directory has been included as an example, otherwise other report directories and files are not committed to the repository.

# Setup
1. A python virtualenv is recommended.
    ```
    pyenv install 3.10.9
    pyenv virtualenv 3.10.9 context-gathering-reporter
    cd ~/My/Directory/Path/context-gathering-reporter
    pyenv local context-gathering-reporter
    ```

2. Make sure to install repository requirements.
    ```
    pip install -r requirements.txt
    ```

For "Today's Stats", context gathering reports are expected to be downloaded in the repository's `/reports` directory:
```
reports/
-- YYYY-MM-DD/
    -- team-file-name.json
```

For Flows teams, this looks like the following for April 2nd, 2024:
```
reports/
-- 2024-04-02/
    -- flows-insight-management.json
    -- information-architecture.json
    -- flows-platform.json
```

# Usage
## Single Report File
### Arguments
- `--summary`: Print the team's high level data
- `--date`: Specify the date to be printed (date is currently not assumed based on file location)

### Examples
To get the report of a single file:
```
> python report_parser.py reports/2024-04-02/flows-platform.json

Domain                        # Missing    %
--------------------------  -----------  ---
flows-debug-tools                     1   5%
flows-evaluations-activity           83  85%
web-feeds                            10  26%
--------------------------  -----------  ---
```

## Today's Reports
### Arguments
- `--summary`: Print high level data at the team level
- `--suppress`: Suppress most errors related to missing files and return what can be found
- `--date`: Pick a different date than today's date in `YYYY-MM-DD` format
- `--duplicates`: Print out any unassigned duplicate domains found. This will still print out the report so using this is recommended in tandem with `--summary`
- `--group`: Print the reports for a known group of teams. An unknown group name will print all downloaded reports. (Ex. `flows`, `mobile`, `integrations`)
    - See [#Groups](#Groups) below

### Examples

To summarize all of today's reports (assuming they've been downloaded in the `reports/YYYY-MM-DD` directory):
```
> python todays_stats.py --summary

2024-04-02

Domain                  # Missing    %
--------------------  -----------  ---
Insight & Management          546  53%
Interface                    1209  47%
Platform                       94  60%
```

To report all of today's reports:
```
> python todays_stats.py

2024-04-02

-  -  -  -  -    -  -  -  -  -  -  -  -  -
F  l  o  w  s    I  n  t  e  r  f  a  c  e
-  -  -  -  -    -  -  -  -  -  -  -  -  -
Domain                                    # Missing    %
--------------------------------------  -----------  ---
ab-navigation-experiment                          1  50%
account-menu                                      1   2%
...
tags                                             15  48%
--------------------------------------  -----------  ---
Total                                          1209  47%

-  -  -  -  -    -  -  -  -  -  -  -    -    -  -  -  -  -  -  -  -  -  -
F  l  o  w  s    I  n  s  i  g  h  t    &    M  a  n  a  g  e  m  e  n  t
-  -  -  -  -    -  -  -  -  -  -  -    -    -  -  -  -  -  -  -  -  -  -
Domain                            # Missing    %
------------------------------  -----------  ---
export-analytics                          7  23%
filter-builder                          273  68%
...
staff-flows-audit                         9   1%
------------------------------  -----------  ---
Total                                   546  53%

-  -  -  -  -    -  -  -  -  -  -  -  -
F  l  o  w  s    P  l  a  t  f  o  r  m
-  -  -  -  -    -  -  -  -  -  -  -  -
Domain                        # Missing    %
--------------------------  -----------  ---
flows-debug-tools                     1   5%
flows-evaluations-activity           83  85%
web-feeds                            10  26%
--------------------------  -----------  ---
Total                                94  60%
```

### Groups
Groups are simply a collection of teams that may be associated with each other. Group definitions can be found in
`constants.py` under `TEAM_GROUPS`. Some groups were best guess approximations.

Current Groups include:
- `flows`:
    - Interface
    - Insight & Management
    - Platform
- `integrations`
    - Advertising Expansion
    - Ecomm SaaS
    - Ecomm Self-Hosted
    - Velocity
- `mobile`
    - Core
    - Push
- `reporting`
    - Reporting
    - Reporting Consistency
- `sms`
    - Compliance Automation
    - Delivery
    - Market Expansion