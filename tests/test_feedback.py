# test_feedback.py
import unittest
from gui import get_password_feedback, format_feedback, split_estimates

class TestFeedbackFunctions(unittest.TestCase):
    def test_empty_password(self):
        hints = get_password_feedback("")
        self.assertIn("Password is empty", hints[0])

    def test_simple_password(self):
        hints = get_password_feedback("abc123")
        self.assertIn("Contains digits.", hints)
        self.assertIn("Length: 6 characters", hints[0] or hints[1])

    def test_format_feedback_actions(self):
        hints = ["Short — consider 12+ characters for better strength."]
        fb_text = format_feedback({}, hints)
        self.assertIn("Actionable steps:", fb_text)

    def test_split_estimates(self):
        estimates = {
            "Per-account throttled (10/hr)": {"seconds": 3600},
            "Offline": {"seconds": 60}
        }
        online, offline = split_estimates(estimates)
        self.assertIn("Per-account throttled", online)
        self.assertIn("Offline", offline)

if __name__ == "__main__":
    unittest.main()
