from constants import TEAM_NAME_TO_FILE_NAME

def get_team_file_name(team: str) -> str:
    return TEAM_NAME_TO_FILE_NAME.get(team, team.lower()) + ".json"