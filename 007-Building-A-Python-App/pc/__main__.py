from .calc import PocketCalculator
from .parser import parse, Token, ParseError


def main_loop():
    calc = PocketCalculator()
    current_op = None
    while True:
        if current_op is None:
            print(calc.value)

        inp = input('>>> ')
        try:
            tok = parse(inp)
        except ParseError as err:
            print(err)
            continue

        if tok is Token.QUIT:
            break
        elif tok is Token.RESET:
            current_op = None
            calc.reset()
        elif tok in [Token.OP_ADD, Token.OP_DIV, Token.OP_MUL, Token.OP_SUB]:
            current_op = tok
        elif tok is Token.NUM:
            n = int(inp.strip())
            if current_op is None:
                calc.set(n)
            else:
                if current_op == Token.OP_ADD:
                    calc.add(n)
                elif current_op == Token.OP_SUB:
                    calc.sub(n)
                elif current_op == Token.OP_MUL:
                    calc.mul(n)
                elif current_op == Token.OP_DIV:
                    calc.div(n)
                current_op = None

    print('Bye')


if __name__ == "__main__":
    main_loop()
