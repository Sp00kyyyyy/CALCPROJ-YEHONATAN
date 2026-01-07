from binary_operator import BinaryOperator
from enums import OperatorType


class Modulo(BinaryOperator):
    def __init__(self):
        super().__init__("%", 4, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        if right == 0:
            raise ZeroDivisionError()
        return left % right
