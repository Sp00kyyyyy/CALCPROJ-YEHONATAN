from unary_operator import UnaryOperator
from enums import OperatorType


class UnaryMinus(UnaryOperator):
    """אופרטור מינוס חד־ערכי."""
    
    def __init__(self):
        """אתחול אופרטור מינוס חד־ערכי."""
        super().__init__("-", 2.5, OperatorType.PREFIX)

    def calculate(self, operand: float) -> float:
        """החזרת הערך השלילי של המספר."""
        return -operand
