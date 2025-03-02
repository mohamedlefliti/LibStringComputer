# laser_string_computer.py

class LaserStringComputer:
    def __init__(self):
        """
        إنشاء كائن للحاسوب الوتري الليزري.
        """
        pass

    def convert_to_frequencies(self, data):
        """
        تحويل البيانات إلى ترددات اهتزازية.
        """
        return [item[0] for item in data]

    def calculate_interference(self, freq1, freq2):
        """
        حساب التداخل بين ترددات مختلفة.
        """
        return abs(freq1 - freq2)

    def optimize_placement(self, components):
        """
        إيجاد الترتيب الأمثل للمكونات بناءً على المسافة، الطاقة، والحرارة.
        """
        from itertools import permutations

        best_order = None
        best_score = float('inf')

        for order in permutations(components):
            total_distance = 0
            total_power = sum(item[1] for item in order)
            total_heat = sum(item[2] for item in order)

            # حساب المسافة الإجمالية
            for i in range(len(order) - 1):
                distance = self.calculate_interference(order[i][0], order[i + 1][0])
                total_distance += distance

            # حساب التكلفة الإجمالية
            score = total_distance + total_power + total_heat

            # تحديث الترتيب الأمثل
            if score < best_score:
                best_score = score
                best_order = order

        return best_order, best_score

    def knapsack_problem(self, items, capacity):
        """
        حل مسألة الحقيبة باستخدام الحاسوب الوتري الليزري.
        """
        best_value = 0
        best_combination = []

        from itertools import combinations

        for r in range(1, len(items) + 1):
            for combination in combinations(items, r):
                total_weight = sum(item[0] for item in combination)
                total_value = sum(item[1] for item in combination)

                if total_weight <= capacity and total_value > best_value:
                    best_value = total_value
                    best_combination = combination

        return best_combination, best_value