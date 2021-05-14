import sly
from sly import Lexer

#Creating the lexer for our programming language

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
    lexer = ptLexer()

    while True:
        try:
            text = input('Parsertongue > ')
        except EOFError:
            break
        if text:
            lexx = lexer.tokenize(text)
            for token in lexx:
              print('type = %r, value = %r' % (token.type, token.value))
