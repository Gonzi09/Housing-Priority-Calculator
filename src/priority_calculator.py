"""
HW 1: Housing Priority Calculator - Priority Calculator Module

This module contains the HousingPriorityCalculator class 
responsible for calculating priority scores.

Implement each method as described in the handout.
"""

class HousingPriorityCalculator:
    """Class responsible for calculating priority scores based on student information."""

    def points_for_class_year(self, year: int) -> int:
        
        points = 0
        
        if year == 1:
            return points
        elif year == 2:
            points = 10
        elif year == 3:
            points = 20
        elif year == 4:
            points = 30
        return points


    def points_for_graduation(self, is_graduating: bool) -> int:
        points = 0
        if is_graduating:
            points = 20

        return points

    def points_for_credits(self, num_credits: int) -> int:
        """
        Compute points based on credits earned.

        Example systems:
        - 1 point per credit
        - 0.5 points per credit
        - Tiered system: 0-30 credits = 1pt each, 31+ = 2pts each
        - Maximum cap: up to 50 credits count

        Here, you may assume num_credits is a non-negative integer,
        since we already validated input in the question asker.

        Document your system in SUMMARY.md!
        
        Implement points system for credits.

        """
        points = 0

        if num_credits >= 0 and num_credits <= 29:
            return points

        elif num_credits >= 30 and num_credits <= 59:
            points = 10

        elif num_credits >= 60 and num_credits <= 89:
            points = 30

        elif num_credits >= 90:
            points = 45
        return points

    def points_for_additional_questions(self, responses: dict[str, bool]) -> int:
        """
        Given the dict from ask_additional_questions(), assign points.
        """
        points = 0
        if responses['at_least_21']:
            points += 5
        if responses['honors']:
            points += 5
        if responses['probation'] is False:
            points +=3
        
        return points

    
    def calculate_total_score(
        self,
        year: int,
        is_graduating: bool,
        num_credits: int,
        additional_responses: dict[str, bool],
    ) -> int:

        total = (
            self.points_for_class_year(year)
            + self.points_for_graduation(is_graduating)
            + self.points_for_credits(num_credits)
            + self.points_for_additional_questions(additional_responses)
        )

        return total
