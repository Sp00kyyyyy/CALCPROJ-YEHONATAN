from binary_operator import BinaryOperator
from enums import OperatorType


class Multiply(BinaryOperator):
    """אופרטור כפל."""
    
    def __init__(self):
        """אתחול אופרטור כפל."""
        super().__init__("*", 2, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """כפל שני מספרים."""
        return left * right
