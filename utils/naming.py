from constants import FILE_NAME_TO_TEAM_NAME, TEAM_NAME_TO_FILE_NAME

def get_team_file_name(team: str) -> str:
    return TEAM_NAME_TO_FILE_NAME.get(team, team.lower().replace(" ", "-")) + ".json"

def get_team_name_from_file_name(file_name: str) -> str:
    no_extension = file_name.replace('.json', '')
    return FILE_NAME_TO_TEAM_NAME.get(no_extension, no_extension.replace("-", " ").title())