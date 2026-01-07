from binary_operator import BinaryOperator
from enums import OperatorType
from exceptions import DivisionByZeroError


class Divide(BinaryOperator):
    """אופרטור חילוק."""
    
    def __init__(self):
        """אתחול אופרטור חילוק."""
        super().__init__("/", 2, OperatorType.INFIX)

    def calculate(self, left: float, right: float) -> float:
        """חילוק שני מספרים."""
        if right == 0:
            raise DivisionByZeroError
        return left / right
