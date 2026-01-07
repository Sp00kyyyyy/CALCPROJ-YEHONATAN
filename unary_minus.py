from unary_operator import UnaryOperator
from enums import OperatorType


class UnaryMinus(UnaryOperator):
    def __init__(self):
        super().__init__("-", 3, OperatorType.PREFIX)

    def calculate(self, operand: float) -> float:
        return -operand
