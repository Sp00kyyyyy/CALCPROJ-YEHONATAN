from binary_operator import BinaryOperator
from enums import OperatorType


class Average(BinaryOperator):
    """אופרטור ממוצע."""
    
    def __init__(self):
        """אתחול אופרטור ממוצע."""
        super().__init__("@", 5, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """חישוב ממוצע בין שני ערכים."""
        return (left + right) / 2
