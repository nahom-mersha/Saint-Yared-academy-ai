import os
import unittest
from pathlib import Path

import NM_fall_back as fallback
import NM_initial_chat_setup as setup
import NM_intents_searcher as searcher
import NM_state_detector as detector


class TestChatbotLogic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The application loads JSON files relative to the backend folder.
        os.chdir(Path(__file__).resolve().parents[1])

    def test_positive_intent_is_detected(self):
        result = searcher.extract_possible_intents("Yes")
        self.assertEqual(result, ["positive_accept_confirm"])

    def test_unknown_text_has_no_intent(self):
        result = searcher.extract_possible_intents("I do not understand")
        self.assertEqual(result, [])

    def test_valid_intent_advances_state(self):
        result = detector.get_state(
            ["positive_accept_confirm"],
            0,
            "ask_about_academy_knowledge",
            [],
        )
        self.assertEqual(result, "give_academy_info_ask_visited_lalibela")

    def test_invalid_intent_uses_soft_fallback(self):
        result = detector.get_state(
            ["negative_decline_not_confirm"],
            0,
            "give_lalibela_info_ask_elevation_estimate",
            [],
        )
        self.assertEqual(result, "soft_fall_back")

    def test_fallback_count_increases(self):
        result = fallback.update_fb_count("soft_fall_back", 1)
        self.assertEqual(result, 2)

    def test_initial_state_and_fallback_limit(self):
        self.assertEqual(setup.get_initial_state(), "greet_and_ask_name")
        self.assertEqual(setup.get_max_fallback_count(), 3)


if __name__ == "__main__":
    unittest.main()