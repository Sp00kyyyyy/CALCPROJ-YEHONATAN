import exceptions
from operator_resolver import OperatorResolver


class PostValidator:
    @staticmethod
    def correct_tilda(tokens: list) -> None:
        for i in range(len(tokens)):
            if tokens[i] != "~":
                continue
            if i == len(tokens) - 1:
                raise exceptions.InvalidSyntaxError
            j = i + 1
            while j < len(tokens) and tokens[j] == "-":
                j += 1
            if j == len(tokens):
                raise exceptions.InvalidSyntaxError
            if not (tokens[j] == "(" or isinstance(tokens[j], float)):
                raise exceptions.InvalidSyntaxError

    @staticmethod
    def correct_unary_minus(tokens: list) -> None:
        for i in range(len(tokens)):
            if tokens[i] != "-":
                continue
            if i == 0:
                if len(tokens) == 1:
                    raise exceptions.InvalidSyntaxError
                if tokens[i + 1] not in ("-", "(", "~") and tokens[i + 1] not in "0123456789":
                    raise exceptions.InvalidSyntaxError
                continue
            prev_token = tokens[i - 1]
            if prev_token == "(" or OperatorResolver.is_operator(prev_token):
                if i == len(tokens) - 1:
                    raise exceptions.InvalidSyntaxError
                if tokens[i + 1] not in ("-", "(", "~") and tokens[i + 1] not in "0123456789":
                    raise exceptions.InvalidSyntaxError
            else:
                if i == len(tokens) - 1:
                    raise exceptions.InvalidSyntaxError
                if tokens[i + 1] not in ("-", "(", "~") and tokens[i + 1] not in "0123456789":
                    raise exceptions.InvalidSyntaxError

    @staticmethod
    def correct_factorial(tokens: list) -> None:
        for i in range(len(tokens)):
            if tokens[i] == "!":
                if i == 0:
                    raise exceptions.InvalidSyntaxError
                prev_token = tokens[i - 1]
                if prev_token == "(" or prev_token in "+-*/^%$&@~":
                    raise exceptions.InvalidSyntaxError
                if prev_token == "!":
                    raise exceptions.InvalidSyntaxError
                if i != len(tokens) - 1:
                    next_token = tokens[i + 1]
                    if next_token not in "+-*/^%$&@)":
                        raise exceptions.InvalidSyntaxError

    @staticmethod
    def validate_binary_operators(tokens: list) -> None:
        binary_ops = "+*/^%$&@-"

        for i in range(len(tokens)):
            token = tokens[i]
            if token in binary_ops:
                if i == 0 or i == len(tokens) - 1:
                    raise exceptions.InvalidSyntaxError
                left = tokens[i - 1]
                right = tokens[i + 1]
                if OperatorResolver.is_operator(left) and left not in ")!":
                    raise exceptions.InvalidSyntaxError
                if OperatorResolver.is_operator(right) and right not in "(~-":
                    raise exceptions.InvalidSyntaxError

    @staticmethod
    def validate_parentheses_context(tokens: list) -> None:
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "(":
                if i > 0:
                    prev_token = tokens[i - 1]
                    if not OperatorResolver.is_operator(prev_token) and prev_token != "(":
                        raise exceptions.InvalidSyntaxError
            if token == ")":
                if i == 0:
                    raise exceptions.InvalidSyntaxError
                prev_token = tokens[i - 1]
                if OperatorResolver.is_operator(prev_token) and prev_token != "!":
                    raise exceptions.InvalidSyntaxError
                if prev_token == "(":
                    raise exceptions.InvalidSyntaxError

    @staticmethod
    def validate(tokens: list) -> None:
        PostValidator.correct_tilda(tokens)
        PostValidator.correct_unary_minus(tokens)
        PostValidator.correct_factorial(tokens)
        PostValidator.validate_binary_operators(tokens)
        PostValidator.validate_parentheses_context(tokens)
