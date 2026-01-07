from abc import abstractmethod
from base_operator import Operator
from enums import OperatorType


class BinaryOperator(Operator):
    """מחלקת בסיס לאופרטורים בינאריים."""
    
    def __init__(self, symbol: str, precedence: float, operator_type: OperatorType):
        """אתחול אופרטור בינארי."""
        super().__init__(symbol, precedence, operator_type)

    @abstractmethod
    def calculate(self, left: float, right: float) -> float:
        """חישוב תוצאת האופרטור הבינארי."""
        pass
