from fileinput import close

from operator_factory import OperatorFactory
from operator_resolver import OperatorResolver
from operator import Operator
from typing import Any
from enums import OperatorType


class ExpressionSolver:
    def __init__(self, tokens: list):
        self.tokens = tokens

    def _find_highest_precedence(self) -> int:
        priority_index: int = 0
        highest_precedence: int = 0
        prev_token: Any = None
        token: Any
        for i in range(len(self.tokens)):
            token = self.tokens[i]
            if OperatorResolver.is_operator(str(token)):
                temp_op: Operator = OperatorFactory.create(token, OperatorResolver.resolve(token, prev_token))
                if temp_op.precedence > highest_precedence:
                    highest_precedence = temp_op.precedence
                    priority_index = i
            prev_token = token
        return priority_index

    def _execute_operation(self, index: int) -> float:
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
            found_num: bool = False
            for i in range(index, -1, -1):
                if isinstance(self.tokens[i], float) and found_num == False:
                    result = temp_op.calculate(self.tokens[i])
                    found_num = True
        else:
            found_num: bool = False
            for i in range(index + 1, len(self.tokens)):
                if isinstance(self.tokens[i], float) and found_num == False:
                    result = temp_op.calculate(self.tokens[i])
                    found_num = True
        return result

    def _replace_with_result(self, index: int, result: float) -> None:
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
            del self.tokens[index: index + 2]
            self.tokens.insert(index, float(result))
        else:
            del self.tokens[index - 1: index + 1]
            self.tokens.insert(index - 1, float(result))

    def solve_parentheses(self) -> None:
        open_index: int = -1
        close_index: int = -1
        open_found: bool = False
        while "(" in self.tokens:
            for i in range(len(self.tokens)):
                if self.tokens[i] == "(" and open_found == False:
                    open_index = i
                    open_found = True
                if self.tokens[i] == ")":
                    close_index = i
            sub_tokens = self.tokens[open_index + 1: close_index]
            sub_result = ExpressionSolver(sub_tokens).solve()
            self.tokens[open_index: close_index + 1] = [sub_result]

    def solve(self) -> float:
        while len(self.tokens) != 1:
            self.solve_parentheses()
            index = self._find_highest_precedence()
            self._replace_with_result(index, self._execute_operation(index))
        return self.tokens[0]
