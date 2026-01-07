from binary_operator import BinaryOperator
from enums import OperatorType


class Modulo(BinaryOperator):
    """אופרטור שארית."""
    
    def __init__(self):
        """אתחול אופרטור שארית."""
        super().__init__("%", 4, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """חישוב שארית החלוקה."""
        if right == 0:
            raise ZeroDivisionError()
        return left % right
