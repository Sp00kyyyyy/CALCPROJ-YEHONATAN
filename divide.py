from binary_operator import BinaryOperator
from enums import OperatorType, Association
from exceptions import DivisionByZeroError


class Divide(BinaryOperator):
    def __init__(self):
        super().__init__("/", 2, OperatorType.INFIX, Association.LEFT)

    def calculate(self, left: float, right: float) -> float:
        if right == 0:
            raise DivisionByZeroError
        return left / right
