from binary_operator import BinaryOperator
from enums import OperatorType


class Multiply(BinaryOperator):
    def __init__(self):
        super().__init__("*", 2, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        return left * right
