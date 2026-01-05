from abc import abstractmethod
from operator import Operator
from enums import OperatorType, Association


class BinaryOperator(Operator):
    def __init__(self, symbol: str, precedence: int, operator_type: OperatorType, association: Association):
        super().__init__(symbol, precedence, operator_type, association)

    @abstractmethod
    def calculate(self, left: float, right: float) -> float:
        pass
