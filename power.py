from binary_operator import BinaryOperator
from enums import OperatorType, Association


class Power(BinaryOperator):
    def __init__(self):
        super().__init__("^", 3, OperatorType.INFIX, Association.RIGHT)

    def calculate(self, left: float, right: float) -> float:
        return pow(left, right)
