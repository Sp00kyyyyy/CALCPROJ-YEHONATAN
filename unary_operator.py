from abc import abstractmethod
from base_operator import Operator
from enums import OperatorType


class UnaryOperator(Operator):
    """מחלקת בסיס לאופרטורים חד־ערכיים."""
    
    def __init__(self, symbol: str, precedence: float, operator_type: OperatorType):
        """אתחול אופרטור חד־ערכי."""
        super().__init__(symbol, precedence, operator_type)

    @abstractmethod
    def calculate(self, operand: float) -> float:
        """חישוב תוצאת האופרטור החד־ערכי."""
        pass
