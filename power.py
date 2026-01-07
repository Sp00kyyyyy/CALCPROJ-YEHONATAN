from binary_operator import BinaryOperator
from enums import OperatorType


class Power(BinaryOperator):
    def __init__(self):
        super().__init__("^", 3, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        return pow(left, right)
