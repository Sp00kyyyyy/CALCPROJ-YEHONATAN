from operator_factory import OperatorFactory
from operator_resolver import OperatorResolver
from base_operator import Operator
from typing import Any
from enums import OperatorType
import exceptions


class ExpressionSolver:
    """פותר ביטויים מתמטיים."""
    
    def __init__(self, tokens: list):
        """אתחול פותר ביטויים."""
        self.tokens = tokens

    def _find_highest_precedence(self) -> int:
        """מציאת האופרטור בעל העדיפות הגבוהה ביותר."""
        priority_index: int = 0
        highest_precedence: float = 0
        prev_token: Any = None
        token: Any
        for i in range(len(self.tokens)):
            token = self.tokens[i]
            if isinstance(token, str) and OperatorResolver.is_operator(token):
                temp_op: Operator = OperatorFactory.create(token, OperatorResolver.resolve(token, prev_token))
                if temp_op.precedence > highest_precedence:
                    highest_precedence = temp_op.precedence
                    priority_index = i
            prev_token = token
        return priority_index

    def _execute_operation(self, index: int) -> float:
        """ביצוע פעולה באינדקס נתון."""
        operator: str = self.tokens[index]
        if index > 0:
            op_type: OperatorType = OperatorResolver.resolve(operator, self.tokens[index - 1])
        else:
            op_type: OperatorType = OperatorResolver.resolve(operator, None)
        temp_op: Operator = OperatorFactory.create(operator, op_type)
        temp_op_type: OperatorType = temp_op.operator_type
        result: float = -1.00123

        if temp_op_type == OperatorType.INFIX:
            result = temp_op.calculate(self.tokens[index - 1], self.tokens[index + 1])
        elif temp_op_type == OperatorType.POSTFIX:
            result = temp_op.calculate(self.tokens[index - 1])
        else:
            next_index = index + 1

            if next_index >= len(self.tokens):
                raise exceptions.InvalidSyntaxError

            next_token = self.tokens[next_index]

            if isinstance(next_token, float):
                result = temp_op.calculate(next_token)
            elif next_token == "-":
                minus_count = 0
                j = next_index
                while j < len(self.tokens) and self.tokens[j] == "-":
                    minus_count += 1
                    j += 1

                if j >= len(self.tokens):
                    raise exceptions.InvalidSyntaxError

                operand = self.tokens[j]
                if isinstance(operand, float):
                    if minus_count % 2 == 1:
                        operand = -operand
                    result = temp_op.calculate(operand)
                else:
                    raise exceptions.InvalidSyntaxError
            elif next_token == "(":
                result = temp_op.calculate(self.tokens[next_index])
            else:
                raise exceptions.InvalidSyntaxError

        return result

    def _replace_with_result(self, index: int, result: float) -> None:
        """החלפת אופרטור ואופרנדים בתוצאה."""
        operator: str = self.tokens[index]
        if index > 0:
            op_type: OperatorType = OperatorResolver.resolve(operator, self.tokens[index - 1])
        else:
            op_type: OperatorType = OperatorResolver.resolve(operator, None)
        temp_op: Operator = OperatorFactory.create(operator, op_type)
        temp_op_type: OperatorType = temp_op.operator_type

        if temp_op_type == OperatorType.INFIX:
            del self.tokens[index - 1: index + 2]
            self.tokens.insert(index - 1, float(result))
        elif temp_op_type == OperatorType.POSTFIX:
            del self.tokens[index - 1: index + 1]
            self.tokens.insert(index - 1, float(result))
        else:
            next_index = index + 1

            if next_index >= len(self.tokens):
                raise exceptions.InvalidSyntaxError

            next_token = self.tokens[next_index]

            if isinstance(next_token, float):
                del self.tokens[index: index + 2]
                self.tokens.insert(index, float(result))
            elif next_token == "-":
                j = next_index
                while j < len(self.tokens) and self.tokens[j] == "-":
                    j += 1

                del self.tokens[index: j + 1]
                self.tokens.insert(index, float(result))
            elif next_token == "(":
                del self.tokens[index: index + 2]
                self.tokens.insert(index, float(result))
            else:
                raise exceptions.InvalidSyntaxError

    def solve_parentheses(self) -> None:
        """פתרון ביטויים בסוגריים."""
        while "(" in self.tokens:
            open_index: int = -1
            close_index: int = -1
            for i in range(len(self.tokens)):
                if self.tokens[i] == "(":
                    open_index = i
                elif self.tokens[i] == ")" and open_index != -1:
                    close_index = i
                    break
            sub_tokens = self.tokens[open_index + 1: close_index]
            sub_result = ExpressionSolver(sub_tokens).solve()
            self.tokens[open_index: close_index + 1] = [sub_result]

    def solve(self) -> float:
        """פתרון הביטוי המלא."""
        while len(self.tokens) != 1:
            self.solve_parentheses()
            index = self._find_highest_precedence()
            self._replace_with_result(index, self._execute_operation(index))
        return self.tokens[0]
