from flask import Blueprint, request
from controllers import OneRepCalculatorController


one_rep_calculator_blueprint = Blueprint("one_rep_calculator_blueprint", __name__)
calculator_controller = OneRepCalculatorController.OneRepCalculatorController()


@one_rep_calculator_blueprint.route("/api/calculateOneRepMax", methods=["GET"])
def calculate_one_rep_max():
    request_body = request.get_json()
    return calculator_controller.calculate_one_rep_max(request_body)
