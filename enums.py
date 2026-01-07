from enum import Enum, auto


class OperatorType(Enum):
    """סוגי אופרטורים אפשריים."""
    INFIX = auto()
    POSTFIX = auto()
    PREFIX = auto()
