from unittest import TestCase
from utils.naming import get_team_file_name, get_team_name_from_file_name

from constants import CCC_TEAM_NAME, FLOWS_IM_TEAM_NAME, TEAM_NAME_TO_FILE_NAME

class TestGetTeamFileName(TestCase):
    def test_get_team_file_name_generic_one_word(self):
        self.assertEqual(get_team_file_name("team1"), "team1.json")
        self.assertEqual(get_team_file_name("team2"), "team2.json")
    
    def test_get_team_file_name_generic_multiple_words(self):
        self.assertEqual(get_team_file_name("team one"), "team-one.json")
        self.assertEqual(get_team_file_name("team two two"), "team-two-two.json")

    def test_defined_team_name(self):
        self.assertEqual(get_team_file_name(CCC_TEAM_NAME), TEAM_NAME_TO_FILE_NAME[CCC_TEAM_NAME] + ".json")
        self.assertEqual(get_team_file_name(FLOWS_IM_TEAM_NAME), TEAM_NAME_TO_FILE_NAME[FLOWS_IM_TEAM_NAME] + ".json")

class TestGetTeamNameFromFileName(TestCase):
    def test_get_team_from_file_name_generic_one_word(self):
        self.assertEqual(get_team_name_from_file_name("team1.json"), "Team1")
        self.assertEqual(get_team_name_from_file_name("team2.json"), "Team2")
    
    def test_get_team_from_file_name_generic_multiple_words(self):
        self.assertEqual(get_team_name_from_file_name("team-one.json"), "Team One")
        self.assertEqual(get_team_name_from_file_name("team-two-two.json"), "Team Two Two")

    def test_defined_team_name(self):
        self.assertEqual(get_team_name_from_file_name(TEAM_NAME_TO_FILE_NAME[CCC_TEAM_NAME] + ".json"), CCC_TEAM_NAME)
        self.assertEqual(get_team_name_from_file_name(TEAM_NAME_TO_FILE_NAME[FLOWS_IM_TEAM_NAME] + ".json"), FLOWS_IM_TEAM_NAME)