from binary_operator import BinaryOperator
from enums import OperatorType


class Maximum(BinaryOperator):
    def __init__(self):
        super().__init__("$", 5, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        max_number: float = 0
        if left >= right:
            max_number = left
        else:
            max_number = right
        return max_number
