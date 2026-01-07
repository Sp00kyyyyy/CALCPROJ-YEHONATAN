import exceptions
from operator_resolver import OperatorResolver
from operator_factory import OperatorFactory


class PostValidator:
    """מאמת ביטויים אחרי פירוק לאסימונים."""
    
    @staticmethod
    def correct_tilda(tokens: list) -> None:
        """בדיקת תקינות אופרטור טילדה."""
        for i in range(len(tokens)):
            if tokens[i] != "~":
                continue
            if i == len(tokens) - 1:
                raise exceptions.InvalidSyntaxError
            if tokens[i + 1] == "-":
                if i + 2 >= len(tokens):
                    raise exceptions.InvalidSyntaxError
                if tokens[i + 2] == "-":
                    raise exceptions.InvalidSyntaxError
                if not (tokens[i + 2] == "(" or isinstance(tokens[i + 2], float)):
                    raise exceptions.InvalidSyntaxError
                continue
            if tokens[i + 1] == "(" or isinstance(tokens[i + 1], float):
                continue
            raise exceptions.InvalidSyntaxError

    @staticmethod
    def correct_unary_minus(tokens: list) -> None:
        """בדיקת תקינות אופרטור מינוס חד־ערכי."""
        for i in range(len(tokens)):
            if tokens[i] != "-":
                continue

            if i == 0:
                if len(tokens) == 1:
                    raise exceptions.InvalidSyntaxError
                if isinstance(tokens[i + 1], str) and OperatorResolver.is_operator(tokens[i + 1]) and tokens[
                    i + 1] not in ("-", "(", "~"):
                    raise exceptions.InvalidSyntaxError
                continue

            prev_token = tokens[i - 1]

            if isinstance(prev_token, str) and (
                    prev_token == "(" or (OperatorResolver.is_operator(prev_token) and prev_token != "-")):
                if i == len(tokens) - 1:
                    raise exceptions.InvalidSyntaxError
                if isinstance(tokens[i + 1], str) and OperatorResolver.is_operator(tokens[i + 1]) and tokens[
                    i + 1] not in ("-", "(", "~"):
                    raise exceptions.InvalidSyntaxError
                continue

            if i == len(tokens) - 1:
                raise exceptions.InvalidSyntaxError
            if isinstance(tokens[i + 1], str) and OperatorResolver.is_operator(tokens[i + 1]) and tokens[i + 1] not in (
                    "-", "(", "~"):
                raise exceptions.InvalidSyntaxError

    @staticmethod
    def correct_factorial(tokens: list) -> None:
        """בדיקת תקינות אופרטור עצרת."""
        for i in range(len(tokens)):
            if tokens[i] == "!":
                if i == 0:
                    raise exceptions.InvalidSyntaxError
                prev_token = tokens[i - 1]
                if isinstance(prev_token, str) and (prev_token == "(" or prev_token in "+-*/^%$&@~"):
                    raise exceptions.InvalidSyntaxError
                if isinstance(prev_token, str) and prev_token == "!#":
                    raise exceptions.InvalidSyntaxError
                if i != len(tokens) - 1:
                    next_token = tokens[i + 1]
                    if isinstance(next_token, str) and next_token not in "+-*/^%$&@)":
                        raise exceptions.InvalidSyntaxError

    @staticmethod
    def validate_binary_operators(tokens: list) -> None:
        """בדיקת תקינות אופרטורים בינאריים."""
        binary_ops = "+*/^%$&@-"

        for i in range(len(tokens)):
            token = tokens[i]
            if isinstance(token, str) and token in binary_ops:
                if token == "-":
                    if i == 0:
                        continue
                    prev = tokens[i - 1]
                    if isinstance(prev, str) and (OperatorResolver.is_operator(prev) or prev == "("):
                        continue
                if i == 0 or i == len(tokens) - 1:
                    raise exceptions.InvalidSyntaxError
                left = tokens[i - 1]
                right = tokens[i + 1]
                if isinstance(left, str) and OperatorResolver.is_operator(left) and left not in ")!#":
                    raise exceptions.InvalidSyntaxError
                if isinstance(right, str) and OperatorResolver.is_operator(right) and right not in "(~-":
                    raise exceptions.InvalidSyntaxError

    @staticmethod
    def validate_parentheses_context(tokens: list) -> None:
        """בדיקת תקינות סוגריים בהקשר."""
        for i in range(len(tokens)):
            token = tokens[i]

            if isinstance(token, str) and token == "(":
                if i > 0:
                    prev_token = tokens[i - 1]
                    if isinstance(prev_token, str):
                        if not (OperatorResolver.is_operator(prev_token) or prev_token == "("):
                            raise exceptions.InvalidSyntaxError
                    else:
                        raise exceptions.InvalidSyntaxError

            if isinstance(token, str) and token == ")":
                if i == 0:
                    raise exceptions.InvalidSyntaxError
                prev_token = tokens[i - 1]
                if isinstance(prev_token, str):
                    if OperatorResolver.is_operator(prev_token) and prev_token != "!#":
                        raise exceptions.InvalidSyntaxError
                    if prev_token == "(":
                        raise exceptions.InvalidSyntaxError

    @staticmethod
    def validate(tokens: list) -> None:
        """אימות כללי של אסימונים."""
        PostValidator.correct_tilda(tokens)
        PostValidator.correct_unary_minus(tokens)
        PostValidator.correct_factorial(tokens)
        PostValidator.validate_binary_operators(tokens)
        PostValidator.validate_parentheses_context(tokens)
        PostValidator.merge_unary_minuses_with_numbers(tokens)
        PostValidator.correct_digit_sum(tokens)

    @staticmethod
    def correct_digit_sum(tokens: list) -> None:
        """בדיקת תקינות אופרטור סכום ספרות."""
        for i in range(len(tokens)):
            if tokens[i] == "#":
                if i == 0:
                    raise exceptions.InvalidSyntaxError
                prev_token = tokens[i - 1]
                if isinstance(prev_token, str) and (prev_token == "(" or prev_token in "+-*/^%$&@~"):
                    raise exceptions.InvalidSyntaxError
                if isinstance(prev_token, str) and prev_token in "!#":
                    pass
                if i != len(tokens) - 1:
                    next_token = tokens[i + 1]
                    if isinstance(next_token, str) and next_token not in "+-*/^%$&@)#":
                        raise exceptions.InvalidSyntaxError

    @staticmethod
    def merge_unary_minuses_with_numbers(tokens: list) -> None:
        """מיזוג מינוסים חד־ערכיים עם מספרים."""
        i = 0
        while i < len(tokens):
            if tokens[i] == "-":
                is_unary = False

                if i == 0:
                    is_unary = True
                elif i > 0:
                    prev = tokens[i - 1]
                    if isinstance(prev, str):
                        if OperatorResolver.is_operator(prev) and prev not in "!)#":
                            is_unary = True
                        elif prev == "(":
                            is_unary = True

                if is_unary:
                    minus_count = 0
                    j = i
                    while j < len(tokens) and tokens[j] == "-":
                        minus_count += 1
                        j += 1

                    should_merge = False
                    if j < len(tokens) and isinstance(tokens[j], float):
                        should_merge = True
                        if j + 1 < len(tokens):
                            next_token = tokens[j + 1]
                            if isinstance(next_token, str) and OperatorResolver.is_operator(next_token):

                                temp_op = OperatorFactory.create(next_token,
                                                                 OperatorResolver.resolve(next_token, tokens[j]))
                                if temp_op.precedence > 2.5:
                                    should_merge = False

                        if should_merge:
                            number = tokens[j]
                            if minus_count % 2 == 1:
                                number = -number

                            del tokens[i:j + 1]
                            tokens.insert(i, number)
                            i = i
                        else:
                            i += 1
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1
