import pytest
from pytest_bdd import scenarios, when, then
from models import OneRepCalculator


# path to feature file
scenarios("../features/one_rep_calculator.feature", example_converters=dict(
        weight_lifted=int,
        num_reps=int,
        one_rep_max=int
    )
)


@pytest.fixture
@when('a user requests to calculate his/her one rep max with "<weight_lifted>" and "<num_reps>"')
def one_rep_max_response(weight_lifted, num_reps):
    calculator = OneRepCalculator.OneRepCalculator()
    return calculator.calculate_one_rep_max(weight_lifted, num_reps)


@pytest.fixture
@then('the model responds with the correct "<one_rep_max>"')
def test_one_rep_max_response(one_rep_max_response, one_rep_max):
    actual = one_rep_max_response
    expected = one_rep_max
    assert actual == expected
