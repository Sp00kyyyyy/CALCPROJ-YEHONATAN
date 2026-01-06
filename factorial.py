from unary_operator import UnaryOperator
from enums import OperatorType, Association
from exceptions import InvalidFactorialError


class Factorial(UnaryOperator):
    def __init__(self):
        super().__init__("!", 6, OperatorType.POSTFIX, Association.NONE)

    def calculate(self, operand: float) -> float:
        if (operand - int(operand)) != 0 or operand < 0:
            raise InvalidFactorialError
        factorial_result: float = 1
        for i in range(int(operand), 0, -1):
            factorial_result *= i
        return factorial_result
