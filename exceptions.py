class EmptyExpressionError(Exception):
    def __init__(self):
        self.message = "Expression cannot be empty"
        super().__init__(self.message)


class UnbalancedParenthesesError(Exception):
    def __init__(self):
        self.message = "Unbalanced parentheses"
        super().__init__(self.message)


class InvalidCharacterError(Exception):
    def __init__(self):
        self.message = "Invalid character in expression"
        super().__init__(self.message)


class InvalidSyntaxError(Exception):
    def __init__(self):
        self.message = "Syntax error in expression"
        super().__init__(self.message)


class DivisionByZeroError(Exception):
    def __init__(self):
        self.message = "Cannot divide by zero"
        super().__init__(self.message)


class InvalidFactorialError(Exception):
    def __init__(self):
        self.message = "Factorial is not defined for the given number"
        super().__init__(self.message)
