# This feature is to test the behavior of the OneRepCalculator model object
Feature: Calculate One Rep Max
  As a weight-lifter,
  I want to get an estimate of my one rep max,
  So I can know whether or not my workout routine is increasing my overall strength.

  Scenario Outline: Calculate One Rep Max Based on Previous Sets and Reps
    When a user requests to calculate his/her one rep max with "<weight_lifted>" and "<num_reps>"
    Then the model responds with the correct "<one_rep_max>"

    Examples:
      | weight_lifted        | num_reps        | one_rep_max        |
      | 255                  | 5               | 287                |
      | 365                  | 5               | 411                |
      | 100                  | 0               | 0                  |
      | 0                    | 100             | 0                  |
      | 0                    | 0               | 0                  |
      | -1                   | -1              | 0                  |