"""
Unit tests for the additional questions in question_asker.
"""
import unittest
from unittest.mock import patch
from src.question_asker import HousingQuestionAsker


class TestAdditionalQuestions(unittest.TestCase):
    """Unit tests for the additional questions in HousingQuestionAsker.
    
    Note: We use patch('builtins.input', ...) to specify user input 
    that would normally be typed. (See impl_hw1.py for more details.)
    
    """

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.question_asker = HousingQuestionAsker()

    def test_ask_additional_questions_basic(self) -> None:
        """Test ask_additional_questions with basic y/n responses."""
        with patch('builtins.input', side_effect=['y', 'n', 'n']):

            # Update these keys based on your actual additional questions:
            # Expected result format: {'question1_key': True, 'question2_key': False}
            # Common examples: 'old23', 'honors', 'athlete', 'work_study', etc.
            responses = {'at_least_21': True, 'honors': False, 'probation': False}
            result = self.question_asker.ask_additional_questions()
            self.assertEqual(result, responses)
            

    def test_ask_additional_questions_reverse(self) -> None:
        """Test ask_additional_questions with n/y responses."""
        with patch('builtins.input', side_effect=['n', 'n', 'y']):
            responses = {'at_least_21': False, 'honors': False, 'probation': True}
            result = self.question_asker.ask_additional_questions()
            self.assertEqual(result, responses)

    def test_ask_additional_questions_uppercase(self) -> None:
        """Test ask_additional_questions with uppercase responses."""
        with patch('builtins.input', side_effect=['Y', 'N', 'Y']):
            result = self.question_asker.ask_additional_questions()
            responses = {'at_least_21': True, 'honors': False, 'probation': True}
            # Test that uppercase Y/N work correctly:
            self.assertEqual(result, responses)

    def test_ask_additional_questions_with_invalid_input(self) -> None:
        """Test ask_additional_questions with some invalid inputs."""
        with patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n', 'maybe', 'y']):
            result = self.question_asker.ask_additional_questions()
            responses = {'at_least_21': True, 'honors': False, 'probation': True}
            self.assertEqual(result, responses)

