import math


class OneRepCalculator:
    def calculate_one_rep_max(self, weight_lifted, num_reps):
        if weight_lifted <= 0 or num_reps <= 0:
            return 0
        one_rep_max = weight_lifted/(1.0278 - 0.0278 * num_reps)
        return math.ceil(one_rep_max)
