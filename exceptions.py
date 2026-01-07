class EmptyExpressionError(Exception):
    """שגיאה כאשר הביטוי ריק."""
    def __init__(self):
        self.message = "Expression cannot be empty"
        super().__init__(self.message)


class UnbalancedParenthesesError(Exception):
    """שגיאה כאשר יש סוגריים לא מאוזנים."""
    def __init__(self):
        self.message = "Unbalanced parentheses"
        super().__init__(self.message)


class InvalidCharacterError(Exception):
    """שגיאה כאשר יש תו לא חוקי בביטוי."""
    def __init__(self):
        self.message = "Invalid character in expression"
        super().__init__(self.message)


class InvalidSyntaxError(Exception):
    """שגיאת תחביר בביטוי."""
    def __init__(self):
        self.message = "Syntax error in expression"
        super().__init__(self.message)


class DivisionByZeroError(Exception):
    """שגיאה כאשר מנסים לחלק באפס."""
    def __init__(self):
        self.message = "Cannot divide by zero"
        super().__init__(self.message)


class InvalidFactorialError(Exception):
    """שגיאה כאשר ערך עצרת לא חוקי."""
    def __init__(self):
        self.message = "Factorial is not defined for the given number"
        super().__init__(self.message)
