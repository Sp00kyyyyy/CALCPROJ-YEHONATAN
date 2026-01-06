from plus import Plus
from minus import Minus
from multiply import Multiply
from divide import Divide
from power import Power
from modulo import Modulo
from maximum import Maximum
from minimum import Minimum
from average import Average
from factorial import Factorial
from negate import Negate
from unary_minus import UnaryMinus
from enums import OperatorType
from operator import Operator


class OperatorFactory:
    REGISTRY: dict = {"+": Plus, "-": [Minus, UnaryMinus], "*": Multiply, "/": Divide, "^": Power, "%": Modulo,
                      "$": Maximum, "&": Minimum, "@": Average, "!": Factorial, "~": Negate}

    @staticmethod
    def create(symbol: str, operator_type: OperatorType) -> Operator:
        if symbol == "-":
            for minus in OperatorFactory.REGISTRY["-"]:
                temp_instance: Operator = minus()
                if temp_instance.operator_type == operator_type:
                    return temp_instance
        else:
            returned_op = OperatorFactory.REGISTRY[symbol]()
            return returned_op
        raise ValueError(f"Operator {symbol} with type {operator_type} not found")
