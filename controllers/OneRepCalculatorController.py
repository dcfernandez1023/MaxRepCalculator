from flask import make_response
from models import OneRepCalculator


class OneRepCalculatorController:
    def __init__(self):
        self.__calculator = OneRepCalculator.OneRepCalculator()

    def calculate_one_rep_max(self, request_body):
        try:
            weight_lifted = int(request_body.get("weight_lifted"))
            num_reps = int(request_body.get("num_reps"))
            one_rep_max = self.__calculator.calculate_one_rep_max(weight_lifted, num_reps)
            return make_response({
                "message": "Success",
                "one_rep_max": one_rep_max
            }, 200)
        except Exception:
            return make_response({"message": "Bad request"}, 400)

