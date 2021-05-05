# This script tests the OneRepCalculatorController object
from controllers import OneRepCalculatorController
from flask import Flask


# test to ensure controller can be instantiated
def test_instantiation():
    controller = OneRepCalculatorController.OneRepCalculatorController()
    assert controller is not None


# test to ensure controller returns OK (200) and the expected calculation
def test_calculate_one_rep_max_controller_response_success():
    test_app = Flask(__name__)
    controller = OneRepCalculatorController.OneRepCalculatorController()
    with test_app.app_context():
        sample_request_body = {"weight_lifted": 255, "num_reps": 5}
        actual = controller.calculate_one_rep_max(sample_request_body)
        status = actual.status_code
        body = actual.get_json()
        assert status == 200 and body.get("one_rep_max") == 287 and body.get("message") == "Success"


# test to ensure controller returns 500 and the expected calculation
def test_calculate_one_rep_max_controller_response_failure():
    test_app = Flask(__name__)
    controller = OneRepCalculatorController.OneRepCalculatorController()
    with test_app.app_context():
        sample_request_body = {"weight_lifted": None, "num_reps": "this is not a valid parameter"}
        actual = controller.calculate_one_rep_max(sample_request_body)
        status = actual.status_code
        body = actual.get_json()
        assert status == 400 and body.get("message") == "Bad request"
