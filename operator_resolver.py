from enums import OperatorType
from typing import Any


class OperatorResolver:
    INFIX_ONLY: str = "+*&^%$@/"
    PREFIX_ONLY: str = "~"
    POSTFIX_ONLY: str = "!"
    OPERATORS: list = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!']

    @staticmethod
    def resolve(token: Any, prev_token: Any | None) -> OperatorType:
        if not (OperatorResolver.is_operator(token)):
            raise ValueError("current token is not an operator")
        elif token in OperatorResolver.INFIX_ONLY:
            return OperatorType.INFIX
        elif token in OperatorResolver.POSTFIX_ONLY:
            return OperatorType.POSTFIX
        elif token in OperatorResolver.PREFIX_ONLY:
            return OperatorType.PREFIX
        if prev_token is None:
            return OperatorType.PREFIX
        elif prev_token in OperatorResolver.OPERATORS:
            return OperatorType.PREFIX
        elif prev_token == "(":
            return OperatorType.PREFIX
        return OperatorType.INFIX

    @staticmethod
    def is_operator(token: str) -> bool:
        return token in OperatorResolver.OPERATORS
