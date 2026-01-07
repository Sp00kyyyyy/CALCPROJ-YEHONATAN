from abc import ABC, abstractmethod
from enums import OperatorType


class Operator(ABC):
    """מחלקת בסיס לאופרטורים."""
    
    def __init__(self, symbol: str, precedence: float, operator_type: OperatorType):
        """אתחול אופרטור בסיס."""
        self.symbol = symbol
        self.precedence = precedence
        self.operator_type = operator_type

    @abstractmethod
    def calculate(self, *operands: float) -> float:
        """חישוב תוצאת האופרטור."""
        pass
