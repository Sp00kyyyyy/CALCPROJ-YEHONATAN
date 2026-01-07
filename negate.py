from unary_operator import UnaryOperator
from enums import OperatorType


class Negate(UnaryOperator):
    """אופרטור שלילה."""
    
    def __init__(self):
        """אתחול אופרטור שלילה."""
        super().__init__("~", 6, OperatorType.PREFIX)

    def calculate(self, operand: float) -> float:
        """החזרת הערך השלילי של המספר."""
        return -operand
