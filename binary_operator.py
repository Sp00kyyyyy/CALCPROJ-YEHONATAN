from abc import abstractmethod
from operator import Operator
from enums import OperatorType


class BinaryOperator(Operator):
    def __init__(self, symbol: str, precedence: float, operator_type: OperatorType):
        super().__init__(symbol, precedence, operator_type)

    @abstractmethod
    def calculate(self, left: float, right: float) -> float:
        pass
