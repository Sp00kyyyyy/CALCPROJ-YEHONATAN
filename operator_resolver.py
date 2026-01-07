from enums import OperatorType
from typing import Any


class OperatorResolver:
    """פותר סוגי אופרטורים."""
    INFIX_ONLY: str = "+*&^%$@/"
    PREFIX_ONLY: str = "~"
    POSTFIX_ONLY: str = "!#"
    OPERATORS: list = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', "#"]

    @staticmethod
    def resolve(token: Any, prev_token: Any | None) -> OperatorType:
        """קביעת סוג האופרטור לפי הקשר."""
        if not isinstance(token, str) or not OperatorResolver.is_operator(token):
            raise ValueError("current token is not an operator")

        if token in OperatorResolver.INFIX_ONLY:
            return OperatorType.INFIX
        if token in OperatorResolver.POSTFIX_ONLY:
            return OperatorType.POSTFIX
        if token in OperatorResolver.PREFIX_ONLY:
            return OperatorType.PREFIX

        if prev_token is None:
            return OperatorType.PREFIX

        if isinstance(prev_token, str):
            if prev_token in OperatorResolver.OPERATORS or prev_token == "(":
                return OperatorType.PREFIX

        return OperatorType.INFIX

    @staticmethod
    def is_operator(token: Any) -> bool:
        """בדיקה אם התו הוא אופרטור."""
        if not isinstance(token, str):
            return False
        return token in OperatorResolver.OPERATORS
