from binary_operator import BinaryOperator
from enums import OperatorType, Association


class Minimum(BinaryOperator):
    def __init__(self):
        super().__init__("&", 5, OperatorType.INFIX, Association.LEFT)

    def calculate(self, left: float, right: float) -> float:
        min_number: float = 0
        if left <= right:
            min_number = left
        else:
            min_number = right
        return min_number
