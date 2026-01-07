from unary_operator import UnaryOperator
from enums import OperatorType
from exceptions import InvalidSyntaxError


class DigitSum(UnaryOperator):
    """אופרטור לחישוב סכום ספרות."""
    
    def __init__(self):
        """אתחול אופרטור סכום ספרות."""
        super().__init__("#", 6, OperatorType.POSTFIX)

    def calculate(self, operand: float) -> float:
        """חישוב סכום ספרות המספר."""
        if operand < 0:
            raise InvalidSyntaxError

        operand_str = str(operand)
        operand_str = operand_str.replace('.', '')

        digit_sum = 0
        for digit in operand_str:
            digit_sum += int(digit)

        return float(digit_sum)
