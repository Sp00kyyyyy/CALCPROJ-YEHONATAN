from enum import Enum, auto


class OperatorType(Enum):
    INFIX = auto()
    POSTFIX = auto()
    PREFIX = auto()


class Association(Enum):
    LEFT = auto()
    RIGHT = auto()
    NONE = auto()
