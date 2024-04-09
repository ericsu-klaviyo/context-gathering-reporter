TABLE_HEADERS = ["Domain", "# Missing", "%"]
TABLE_COLALIGN = ("left","right","right")
TOTAL_STR = "Total"

FLOWS_IM_TEAM_NAME = "Insight & Management"
FLOWS_INTERFACE_TEAM_NAME = "Interface"
FLOWS_PLATFORM_TEAM_NAME = "Platform"

TEAM_NAME_TO_FILE_NAME = {
    FLOWS_IM_TEAM_NAME: "flows-insight-management",
    FLOWS_INTERFACE_TEAM_NAME: "information-architecture",
    FLOWS_PLATFORM_TEAM_NAME: "flows-platform",
}

DOMAIN_OWNERSHIP = {
    "filter-builder": TEAM_NAME_TO_FILE_NAME[FLOWS_IM_TEAM_NAME],
}