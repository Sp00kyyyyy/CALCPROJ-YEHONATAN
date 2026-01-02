class Operator():
    def __init__(self, symbol: str, precedence: int, operator_type: str):
        self.symbol = symbol
        self.precedence = precedence
        self.operator_type = operator_type

    # חובה לממש במחלקות שיורשות
    def calculate(self, *operands: float) -> float: raise NotImplementedError
