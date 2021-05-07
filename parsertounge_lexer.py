import sly
from sly import Lexer

#Creating the lexer for our programming language

#Errors
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

#Lexer Class
class ptLexer(Lexer):

    # Set of token names.   This is always required
    tokens = { TOKEN_INT, TOKEN_PERIOD, TOKEN_SUM, 
              TOKEN_MINUS, TOKEN_IGUAL, TOKEN_X, TOKEN_Y, TOKEN_Z, NEXT_EQUATION, END_SYSTEM }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens

    #Tokens
    TOKEN_INT        = r'\d+'
    TOKEN_PERIOD     = r'\.'
    TOKEN_SUM        = r'\+'
    TOKEN_MINUS      = r'-'
    TOKEN_IGUAL      = r'='
    TOKEN_X          = r'[xX]'
    TOKEN_Y          = r'[yY]'
    TOKEN_Z          = r'[zZ]'
    NEXT_EQUATION    = r'&'
    END_SYSTEM       = r'#'
    
    #Numbers
    @_(r'\d+')
    def TOKEN_INT(self, t):
        t.value = int(t.value)
        return t
    
    #Comments
    #@_(r'#.*')
    #def COMMENT(self, t):
    #    pass

if __name__ == '__main__':
    #equation = '5.6x + 22y - z = 3'
    equation = []
    #equation_2 = [TOKEN_X, TOKEN_Y, TOKEN_Z]
    #equation_3 = [TOKEN_X, TOKEN_Y, TOKEN_Z]
    
    system = "5x+3y-z=6 & 7.2x-8y+1.9z=6.2 & 13y-7.2x+z=4.2 #"
    lexer = ptLexer()
    for tok in lexer.tokenize(system):
        print(tok)

    while True:
        try:
            text = input('Parsertongue > ')
        except EOFError:
            break
        if text:
            lexx = lexer.tokenize(text)
            for token in lexx:
              print('type = %r, value = %r' % (token.type, token.value))
              equation.append(token.value)
            print(f'Equation #1: {equation}')
