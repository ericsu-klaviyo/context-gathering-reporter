REPORTS_BASE_PATH = "reports"

TABLE_HEADERS = ["Domain", "# Missing", "%"]
TABLE_COLALIGN = ("left","right","right")
TOTAL_STR = "Total"

# Give teams custom or specifically formatted names here
APIS_TEAM_NAME = "APIs"
CCC_TEAM_NAME = "Catalog, Coupon, & Custom Objects"
FLOWS_IM_TEAM_NAME = "Insight & Management"
FLOWS_INTERFACE_TEAM_NAME = "Interface"
FLOWS_PLATFORM_TEAM_NAME = "Platform"

# Custom teams names with mismatching file names should be defined here (lowercase, hyphenated)
TEAM_NAME_TO_FILE_NAME = {
    CCC_TEAM_NAME: "ccc",
    FLOWS_IM_TEAM_NAME: "flows-insight-management",
    FLOWS_INTERFACE_TEAM_NAME: "information-architecture",
    FLOWS_PLATFORM_TEAM_NAME: "flows-platform",
}

DOMAIN_OWNERSHIP = {
    "filter-builder": TEAM_NAME_TO_FILE_NAME[FLOWS_IM_TEAM_NAME],
}

FILE_NAME_TO_TEAM_NAME = {v: k for k, v in TEAM_NAME_TO_FILE_NAME.items()}

# Defined team names should be used as values if they exist, otherwise use file names
TEAM_GROUPS = {
    "flows": [FLOWS_IM_TEAM_NAME, FLOWS_INTERFACE_TEAM_NAME, FLOWS_PLATFORM_TEAM_NAME],
    "integrations": [
        "integrations-advertising-expansion",
        "integrations-ecom-saas",
        "integrations-ecom-self-hosted",
        "integrations-velocity"
    ],
    "mobile": [
        "mobile-core",
        "mobile-push-team"
    ],
    "reporting": [
        "reporting-consistency",
        "reporting"
    ],
    "sms": [
        "sms-compliance-automation",
        "sms-delivery",
        "sms-market-expansion",
    ]
}