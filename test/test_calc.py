import pytest
from pre_validator import PreValidator
from tokenizer import Tokenizer
from post_validator import PostValidator
from expression_solver import ExpressionSolver


def run_expression(expression):
    pre_validator = PreValidator()
    pre_validator.validate(expression)
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    PostValidator.validate(tokens)
    solver = ExpressionSolver(tokens)
    return solver.solve()


class TestSyntaxErrors:

    def test_operator_after_operator(self):
        with pytest.raises(Exception):
            run_expression("2*^3")

    def test_missing_operand(self):
        with pytest.raises(Exception):
            run_expression("3+")

    def test_double_binary_operators(self):
        with pytest.raises(Exception):
            run_expression("5++3")

    def test_unbalanced_parentheses_open(self):
        with pytest.raises(Exception):
            run_expression("(3+2")

    def test_unbalanced_parentheses_close(self):
        with pytest.raises(Exception):
            run_expression("3+2)")


class TestInvalidInputs:

    def test_gibberish_string(self):
        with pytest.raises(Exception):
            run_expression("abcxyz")

    def test_empty_string(self):
        with pytest.raises(Exception):
            run_expression("")

    def test_whitespace_only(self):
        with pytest.raises(Exception):
            run_expression("   ")

    def test_tabs_only(self):
        with pytest.raises(Exception):
            run_expression("\t\t\t")

    def test_whitespace_and_tabs(self):
        with pytest.raises(Exception):
            run_expression(" \t \t ")


class TestSimpleExpressions:

    def test_addition(self):
        assert run_expression("3+2") == 5.0

    def test_subtraction(self):
        assert run_expression("5-3") == 2.0

    def test_multiplication(self):
        assert run_expression("4*2") == 8.0

    def test_division(self):
        assert run_expression("10/5") == 2.0

    def test_power(self):
        assert run_expression("2^3") == 8.0

    def test_modulo(self):
        assert run_expression("10%3") == 1.0

    def test_maximum(self):
        assert run_expression("5$3") == 5.0

    def test_minimum(self):
        assert run_expression("5&3") == 3.0

    def test_average(self):
        assert run_expression("4@6") == 5.0

    def test_negate(self):
        assert run_expression("~5") == -5.0

    def test_factorial(self):
        assert run_expression("3!") == 6.0

    def test_unary_minus(self):
        assert run_expression("-5") == -5.0

    def test_digit_sum(self):
        assert run_expression("123#") == 6.0

    def test_double_digit_sum(self):
        assert run_expression("99##") == 9.0

    def test_decimal_digit_sum(self):
        assert run_expression("2.3#") == 5.0


class TestComplexExpressions:

    def test_precedence_multiply_add(self):
        assert run_expression("2+3*4") == 14.0

    def test_precedence_subtract_multiply(self):
        assert run_expression("10-2*3") == 4.0

    def test_power_add(self):
        assert run_expression("2^3+1") == 9.0

    def test_factorial_add(self):
        assert run_expression("3!+2") == 8.0

    def test_multiply_factorial(self):
        assert run_expression("5*2!") == 10.0

    def test_parentheses_multiply(self):
        assert run_expression("(2+3)*4") == 20.0

    def test_multiply_parentheses(self):
        assert run_expression("2*(3+4)") == 14.0

    def test_nested_parentheses(self):
        assert run_expression("((2+3)*4)-5") == 15.0

    def test_unary_minus_factorial(self):
        assert run_expression("-3!") == -6.0

    def test_double_unary_minus_factorial(self):
        assert run_expression("--3!") == 6.0

    def test_unary_minus_power(self):
        assert run_expression("-2^4") == -16.0

    def test_parentheses_unary_minus_power(self):
        assert run_expression("(-2)^4") == 16.0

    def test_triple_minus_factorial(self):
        assert run_expression("2---3!") == -4.0

    def test_negate_with_unary_minus(self):
        assert run_expression("3+~-3") == 6.0

    def test_complex_with_all_operators(self):
        assert run_expression("((2+3)*4)-(5*2)+3!") == 16.0

    def test_maximum_minimum_average(self):
        assert run_expression("(5$3)&(7$2)@(10%3)") == 2.0

    def test_digit_sum_with_operations(self):
        assert run_expression("123#+99##") == 15.0

    def test_negative_digit_sum(self):
        assert run_expression("-123#") == -6.0

    def test_complex_with_spaces(self):
        assert run_expression("( 2 + 3 ) * ( 4 - 1 )") == 15.0

    def test_long_expression_20_chars(self):
        assert run_expression("2^3*4-5+3!*2") == 39.0