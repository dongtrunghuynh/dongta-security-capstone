import unittest
from gui import get_password_feedback, format_feedback

class TestPasswordFeedback(unittest.TestCase):
    def test_weak_password(self):
        password = "password123"
        feedback = get_password_feedback(password)
        self.assertIn("Contains common word or phrase", feedback)
        self.assertIn("Contains a sequence", feedback)
        formatted = format_feedback(feedback)
        self.assertIn("- Contains common word or phrase", formatted)
        self.assertIn("- Contains a sequence", formatted)

    def test_strong_password(self):
        password = "Xy7!mN#2qLp$8z"
        feedback = get_password_feedback(password)
        self.assertEqual(feedback, [])
        formatted = format_feedback(feedback)
        self.assertEqual(formatted, "No specific feedback. Good job!")

    def test_short_password(self):
        password = "aB3!"
        feedback = get_password_feedback(password)
        self.assertIn("Short random-looking password", feedback)
        formatted = format_feedback(feedback)
        self.assertIn("- Short random-looking password", formatted)

    def test_repeated_characters(self):
        password = "aaaaaa"
        feedback = get_password_feedback(password)
        self.assertIn("Contains repeated characters or sequences", feedback)
        formatted = format_feedback(feedback)
        self.assertIn("- Contains repeated characters or sequences", formatted)
        
    def test_empty_password(self):
        password = ""
        feedback = get_password_feedback(password)
        self.assertIn("Short random-looking password", feedback)
        formatted = format_feedback(feedback)
        self.assertIn("- Short random-looking password", formatted)
    
    def test_mixed_cases_and_symbols(self):
        password = "P@ssw0rd!"
        feedback = get_password_feedback(password)
        self.assertIn("Contains common word or phrase", feedback)
        formatted = format_feedback(feedback)
        self.assertIn("- Contains common word or phrase", formatted)
        
    def test_format_feedback_combines_hints(self):
        feedback_dict = {"warning": "Weak password", "suggestions": ["Add symbols"]}
        hints = ["Length: good", "Contains digits"]
        result = format_feedback(feedback_dict, hints)
        self.assertIn("Warning: Weak password", result)
        self.assertIn("Length: good", result)
        self.assertIn("Contains digits", result)
        self.assertIn("Add symbols", result)
        
if __name__ == '__main__':
    unittest.main()