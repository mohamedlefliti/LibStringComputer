# applications.py

from laser_string_computer import LaserStringComputer

class Applications:
    def __init__(self):
        """
        إنشاء كائن لتطبيقات الحاسوب الوتري الليزري.
        """
        self.lsc = LaserStringComputer()

    def chip_design(self, components):
        """
        تحسين تخطيط الرقائق الإلكترونية.
        """
        optimal_placement, total_cost = self.lsc.optimize_placement(components)
        return optimal_placement, total_cost

    def knapsack_solution(self, items, capacity):
        """
        حل مسألة الحقيبة.
        """
        best_combination, best_value = self.lsc.knapsack_problem(items, capacity)
        return best_combination, best_value