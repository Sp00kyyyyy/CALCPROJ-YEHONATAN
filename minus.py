from binary_operator import BinaryOperator
from enums import OperatorType


class Minus(BinaryOperator):
    """אופרטור חיסור."""
    
    def __init__(self):
        """אתחול אופרטור חיסור."""
        super().__init__("-", 1, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """חיסור שני מספרים."""
        return left - right
