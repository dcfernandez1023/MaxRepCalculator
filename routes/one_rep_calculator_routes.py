from flask import Blueprint, request
from controllers import OneRepCalculatorController


one_rep_calculator_blueprint = Blueprint("one_rep_calculator_blueprint", __name__)
calculator_controller = OneRepCalculatorController.OneRepCalculatorController()


@one_rep_calculator_blueprint.route("/api/calculateOneRepMax/<weight_lifted>/<num_reps>", methods=["GET"])
def calculate_one_rep_max(weight_lifted, num_reps):
    req_body = {"weight_lifted": weight_lifted, "num_reps": num_reps}
    return calculator_controller.calculate_one_rep_max(req_body)
