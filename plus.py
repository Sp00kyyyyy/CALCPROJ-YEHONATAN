from binary_operator import BinaryOperator
from enums import OperatorType


class Plus(BinaryOperator):
    """אופרטור חיבור."""
    
    def __init__(self):
        """אתחול אופרטור חיבור."""
        super().__init__("+", 1, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """חיבור שני מספרים."""
        return left + right
