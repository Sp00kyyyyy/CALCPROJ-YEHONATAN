from unary_operator import UnaryOperator
from enums import OperatorType


class Negate(UnaryOperator):
    def __init__(self):
        super().__init__("~", 6, OperatorType.PREFIX)

    def calculate(self, operand: float) -> float:
        return -operand
