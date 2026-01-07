from binary_operator import BinaryOperator
from enums import OperatorType


class Power(BinaryOperator):
    """אופרטור חזקה."""
    
    def __init__(self):
        """אתחול אופרטור חזקה."""
        super().__init__("^", 3, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """חישוב חזקה."""
        return pow(left, right)
