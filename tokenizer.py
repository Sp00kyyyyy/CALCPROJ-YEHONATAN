class Tokenizer:
    """מפרק ביטויים לאסימונים."""
    OPERATORS_AND_PARENTHESES = "+-*/^%$&@~!()#"
    VALID_NUMBER_CHARS = "0123456789."

    def __init__(self, expression: str):
        """אתחול מפרק."""
        self.expression = expression

    def tokenize(self) -> list:
        """פירוק הביטוי לאסימונים."""
        tokens: list = []
        current_number: str = ""
        for char in self.expression:
            if char in Tokenizer.VALID_NUMBER_CHARS:
                current_number += char
            elif char in Tokenizer.OPERATORS_AND_PARENTHESES:
                if current_number != "":
                    try:
                        tokens.append(float(current_number))
                    except ValueError:
                        tokens.append(current_number)
                    current_number = ""
                tokens.append(char)
            elif char == " ":
                if current_number != "":
                    try:
                        tokens.append(float(current_number))
                    except ValueError:
                        tokens.append(current_number)
                    current_number = ""

        if current_number != "":
            try:
                tokens.append(float(current_number))
            except ValueError:
                tokens.append(current_number)
        return tokens
