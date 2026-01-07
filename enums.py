from enum import Enum, auto


class OperatorType(Enum):
    INFIX = auto()
    POSTFIX = auto()
    PREFIX = auto()
