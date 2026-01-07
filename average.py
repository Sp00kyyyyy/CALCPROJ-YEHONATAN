from binary_operator import BinaryOperator
from enums import OperatorType


class Average(BinaryOperator):
    def __init__(self):
        super().__init__("@", 5, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        return (left + right) / 2
