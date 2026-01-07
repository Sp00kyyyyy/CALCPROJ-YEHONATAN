from abc import ABC, abstractmethod
from enums import OperatorType


class Operator(ABC):
    def __init__(self, symbol: str, precedence: float, operator_type: OperatorType):
        self.symbol = symbol
        self.precedence = precedence
        self.operator_type = operator_type

    @abstractmethod
    def calculate(self, *operands: float) -> float:
        """פעולה לחישוב תוצאת האופרטור. חובה ליישם את הפעולה במחלקות היורשות"""
        pass
