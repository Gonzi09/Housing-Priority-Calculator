"""
HW 1: Housing Priority Calculator - Question Asker Module

This module contains the HousingQuestionAsker class responsible for gathering user input.

Step 1: Complete all required items in test_question_asker.py
Step 2: Run tests (they should fail) - this is expected!
Step 3: Implement methods below to make tests pass
Step 4: Run tests again to verify they pass
"""

class HousingQuestionAsker:
    """Class responsible for asking questions and gathering user input."""

    def ask_class_year(self) -> int:
        """Ask for class year"""
        while True:
            try:
                response: int = int(input('What year are you in school? (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior)'))
                if response in [1,2,3,4]:
                    return response
                else:
                    print('Enter a valid number')

            except ValueError:
                print('Invalid input please enter a valid number from the options provided')

    def ask_graduation_status(self) -> bool:
        """Ask if the student is graduating this semester."""

        while True:
            response: str = (input('Are you graduating this semester?')).strip().lower()
            if response == 'y':
                return True
            if response == 'n':
                return False
            print('Invalid input\n Select y/n')

    def ask_credits_earned(self) -> int:
        """Ask for credits earned and return as int."""

        while True:

            try:      
                response = int(input('How many credits have you earned?'))
                if response >= 0:
                    return response
                else:
                    print('Enter a valid non-negative number')
            except ValueError:
                print('Please enter a number')

    def ask_additional_questions(self) -> dict[str, bool]:
        """Ask at least two yes/no questions and return a dict of responses."""

        def yes_no(prompt: str) -> bool:
            """Keeps asking until correct input"""
            while True:
                response = input(prompt + ' y/n: ').strip().lower()
                if response == 'y' or response == 'yes':
                    return True
                if response == 'n' or response == 'no':
                    return False
                print('Invalid input, enter y/n')


        responses = {'at_least_21' : yes_no(('Are you at least 21 years old?')),
                    'honors' : yes_no(('Are you a honors student?')),
                    'probation' : yes_no(('Have you ever been on probation?'))}

        return responses
        
        
                

        