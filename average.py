from binary_operator import BinaryOperator
from enums import OperatorType, Association


class Average(BinaryOperator):
    def __init__(self):
        super().__init__("@", 5, OperatorType.INFIX, Association.LEFT)

    def calculate(self, left: float, right: float) -> float:
        return (left + right) / 2
