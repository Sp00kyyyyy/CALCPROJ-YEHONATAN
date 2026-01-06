from unary_operator import UnaryOperator
from enums import OperatorType, Association


class UnaryMinus(UnaryOperator):
    def __init__(self):
        super().__init__("-", 3, OperatorType.PREFIX, Association.NONE)

    def calculate(self, operand: float) -> float:
        return -operand
