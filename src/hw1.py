"""
HW 1: Housing Priority Calculator - Main Module

This is the main module that orchestrates the housing priority calculation
by using both the HousingQuestionAsker and HousingPriorityCalculator classes.
"""
from src.question_asker import HousingQuestionAsker
from src.priority_calculator import HousingPriorityCalculator

def calculate_score() -> int:
    
    asker = HousingQuestionAsker()
    calculator = HousingPriorityCalculator()

    year = asker.ask_class_year()
    num_credits = asker.ask_credits_earned()
    is_graduating = asker.ask_graduation_status() if year is 4 else False
    additional_responses = asker.ask_additional_questions()

    total = calculator.calculate_total_score(year, is_graduating, num_credits, additional_responses)
    
    return total
def main() -> None:
    """Entry point: print header, compute score, print footer. (For easier readability)"""

    print("===================================")
    print(" Welcome to the Housing Calculator ")
    print("===================================")

    total = calculate_score()


    print(f"\nYour housing priority score is: {total}")

    print("===================================")
    print(" Thank you for using the calculator ")
    print("===================================")

if __name__ == "__main__":
    main()
