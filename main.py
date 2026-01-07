from pre_validator import PreValidator
from tokenizer import Tokenizer
from post_validator import PostValidator
from expression_solver import ExpressionSolver
import exceptions

while True:
    expression: str = input("Enter an expression: ")

    if expression == "S":
        break

    try:
        pre_validator = PreValidator()
        pre_validator.validate(expression)

        tokenizer = Tokenizer(expression)
        tokens = tokenizer.tokenize()
        print("TOKENS:", tokens)

        PostValidator.validate(tokens)


        solver = ExpressionSolver(tokens)
        result = solver.solve()

        print("Result:", result)

    except Exception as e:
        print("Error:", e)