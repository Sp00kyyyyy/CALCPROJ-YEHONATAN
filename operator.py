from abc import ABC, abstractmethod
from enums import OperatorType, Association


class Operator(ABC):
    def __init__(self, symbol: str, precedence: int, operator_type: OperatorType, association: Association):
        self.symbol = symbol
        self.precedence = precedence
        self.operator_type = operator_type
        self.association = association

    @abstractmethod
    def calculate(self, *operands: float) -> float:
        """פעולה לחישוב תוצאת האופרטור. חובה ליישם במחלקות היורשות"""
        pass
