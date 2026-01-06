from exceptions import EmptyExpressionError, InvalidCharacterError, InvalidSyntaxError, UnbalancedParenthesesError


class PreValidator:
    ALLOWED_CHARS: str = "0123456789 .+-*/^%$&@~!()"
    BINARY_ONLY: str = "+*/%^$&@"

    def __init__(self):
        self.is_valid: bool = True

    def is_empty(self, expression: str) -> None:
        if len(expression.strip()) == 0:
            self.is_valid = False
            raise EmptyExpressionError

    def validate_allowed_chars(self, expression: str) -> None:
        for char in expression:
            if char not in PreValidator.ALLOWED_CHARS:
                self.is_valid = False
                raise InvalidCharacterError

    def validate_parentheses(self, expression: str) -> None:
        count = 0
        for char in expression:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
                if count < 0:
                    self.is_valid = False
                    raise InvalidSyntaxError

        if count != 0:
            self.is_valid = False
            raise UnbalancedParenthesesError

    def validate_start(self, expression: str) -> None:
        expression = expression.strip()
        valid_start: str = "0123456789~!(."
        if expression[0] not in valid_start:
            self.is_valid = False
            raise InvalidSyntaxError

    def validate_end(self, expression: str) -> None:
        expression = expression.strip()
        valid_end = "0123456789)~!."
        if expression[len(expression) - 1] not in valid_end:
            self.is_valid = False
            raise InvalidSyntaxError

    def validate_no_double_dot(self, expression: str) -> None:
        expression_no_spaces = expression.replace(" ", "")
        last_char: str = expression_no_spaces[0]
        for char in expression_no_spaces[1:]:
            if char == "." and last_char == ".":
                self.is_valid = False
                raise InvalidSyntaxError
            last_char = char

    def validate_no_double_op(self, expression: str) -> None:
        expression_no_spaces = expression.replace(" ", "")
        last_char: str = expression_no_spaces[0]
        for char in expression_no_spaces[1:]:
            if char in PreValidator.BINARY_ONLY and last_char in PreValidator.BINARY_ONLY:
                self.is_valid = False
                raise InvalidSyntaxError
            last_char = char

    def validate(self, expression: str) -> None:
        self.is_valid = True
        self.is_empty(expression)
        self.validate_start(expression)
        self.validate_allowed_chars(expression)
        self.validate_end(expression)
        self.validate_parentheses(expression)
        self.validate_no_double_dot(expression)
        self.validate_no_double_op(expression)
