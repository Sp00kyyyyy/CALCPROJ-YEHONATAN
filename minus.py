from binary_operator import BinaryOperator
from enums import OperatorType


class Minus(BinaryOperator):
    def __init__(self):
        super().__init__("-", 1, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        return left - right
