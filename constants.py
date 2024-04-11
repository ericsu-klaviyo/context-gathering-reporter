REPORTS_BASE_PATH = "reports"

TABLE_HEADERS = ["Domain", "# Missing", "%"]
TABLE_COLALIGN = ("left","right","right")
TOTAL_STR = "Total"

# Give teams custom or specifically formatted names here
APIS_TEAM_NAME = "APIs"
CCC_TEAM_NAME = "Catalog, Coupon, & Custom Objects"
FLOWS_IM_TEAM_NAME = "Flows Insight & Management"
FLOWS_INTERFACE_TEAM_NAME = "Flows Interface"
FLOWS_PLATFORM_TEAM_NAME = "Flows Platform"
INTEGRATIONS_ECOMM_SAAS_TEAM_NAME = "Integrations eComm SaaS"
INTEGRATIONS_ECOMM_SELF_HOSTED_TEAM_NAME = "Integrations eComm Self-Hosted"
SMS_COMPLIANCE_AUTOMATION_TEAM_NAME = "SMS Compliance Automation"
SMS_DELIVERY_TEAM_NAME = "SMS Delivery"
SMS_MARKET_EXPANSION_TEAM_NAME = "SMS Market Expansion"

# Custom teams names with mismatching file names should be defined here (lowercase, hyphenated)
TEAM_NAME_TO_FILE_NAME = {
    CCC_TEAM_NAME: "ccc",
    FLOWS_IM_TEAM_NAME: "flows-insight-management",
    FLOWS_INTERFACE_TEAM_NAME: "information-architecture",
    FLOWS_PLATFORM_TEAM_NAME: "flows-platform",
    INTEGRATIONS_ECOMM_SAAS_TEAM_NAME: "integrations-ecom-saas",
    INTEGRATIONS_ECOMM_SELF_HOSTED_TEAM_NAME: "integrations-ecom-self-hosted",
    SMS_COMPLIANCE_AUTOMATION_TEAM_NAME: "sms-compliance-automation",
    SMS_DELIVERY_TEAM_NAME: "sms-delivery",
    SMS_MARKET_EXPANSION_TEAM_NAME: "sms-market-expansion",
}

# Define domain ownership for domains that may have been found in multiple teams' reports
DOMAIN_OWNERSHIP = {
    "filter-builder": TEAM_NAME_TO_FILE_NAME[FLOWS_IM_TEAM_NAME],
}

FILE_NAME_TO_TEAM_NAME = {v: k for k, v in TEAM_NAME_TO_FILE_NAME.items()}

# Defined team names should be used as values if they exist, otherwise use expected file names (without .json extension included)
TEAM_GROUPS = {
    "flows": [FLOWS_IM_TEAM_NAME, FLOWS_INTERFACE_TEAM_NAME, FLOWS_PLATFORM_TEAM_NAME],
    "integrations": [
        "integrations-advertising-expansion",
        INTEGRATIONS_ECOMM_SAAS_TEAM_NAME,
        INTEGRATIONS_ECOMM_SELF_HOSTED_TEAM_NAME,
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
        SMS_COMPLIANCE_AUTOMATION_TEAM_NAME,
        SMS_DELIVERY_TEAM_NAME,
        SMS_MARKET_EXPANSION_TEAM_NAME
    ]
}