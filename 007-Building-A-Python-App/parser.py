"""The parser used to parse the user input for the calculator"""

from enum import Enum


class Token(Enum):
    NUM = 'NUM'
    OP_ADD = 'OP_ADD'
    OP_SUB = 'OP_SUB'
    OP_MUL = 'OP_MUL'
    OP_DIV = 'OP_DIV'
    RESET = 'RESET'
    QUIT = 'QUIT'


class ParseError(Exception):
    pass


def parse(inp: str) -> Token:
    inp = inp.strip()
    if inp == '+':
        return Token.OP_ADD
    elif inp == '-':
        return Token.OP_SUB
    elif inp == '*':
        return Token.OP_MUL
    elif inp == '/':
        return Token.OP_DIV
    elif inp == 'q':
        return Token.QUIT
    elif inp == '':
        return Token.RESET
    else:
        try:
            _ = int(inp)
            return Token.NUM
        except:
            raise ParseError(f'Invalid input: {inp}')
