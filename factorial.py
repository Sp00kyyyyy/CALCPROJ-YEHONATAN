from unary_operator import UnaryOperator
from enums import OperatorType
from exceptions import InvalidFactorialError


class Factorial(UnaryOperator):
    """אופרטור עצרת."""
    
    def __init__(self):
        """אתחול אופרטור עצרת."""
        super().__init__("!", 6, OperatorType.POSTFIX)

    def calculate(self, operand: float) -> float:
        """חישוב עצרת של מספר שלם וחיובי."""
        if (operand - int(operand)) != 0 or operand < 0:
            raise InvalidFactorialError
        factorial_result: float = 1
        for i in range(int(operand), 0, -1):
            factorial_result *= i
        return factorial_result
