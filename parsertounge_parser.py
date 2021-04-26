import sly
from sly import Parser
from parsertounge_lexer import ptLexer
import numpy as np

class ptParser(Parser):
    # Get the token list from the lexer (required)
    tokens = ptLexer.tokens

    #Create numpy array to store coefficients/result
    def __init__(self):
        self.coefficients = np.zeros((3, 3))
        self.results = np.zeros((3,1))
        

    
    @_('TOKEN_INT TOKEN_PERIOD TOKEN_INT')
    def number(self, p):
        return p.TOKEN_INT0 + (p.TOKEN_INT1)/((10.0)**(len(str(p.TOKEN_INT1))))
    
    @_('TOKEN_INT')
    def number(self, p):
        return p.TOKEN_INT
    
    @_('TOKEN_MINUS number')
    def number(self, p):
        return p.number * (-1)
    
    @_('TOKEN_SUM number')
    def number(self, p):
        return p.number
    
    @_('number TOKEN_X')
    def x_term(self, p):
        self.coefficents[p.lineno, 0] = float(p.number)
        return p.x_term
        
    @_('TOKEN_SUM TOKEN_X')
    def x_term(self, p):
        self.coefficents[p.lineno, 0] = 1.0
        return p.x_term
        
    @_('TOKEN_MINUS TOKEN_X')
    def x_term(self, p):
        self.coefficents[p.lineno, 0] = -1.0
        return p.x_term
    
    @_('number TOKEN_Y')
    def y_term(self, p):
        self.coefficents[p.lineno, 1] = float(p.number)
        
    @_('TOKEN_SUM TOKEN_Y')
    def y_term(self, p):
        self.coefficents[p.lineno, 1] = 1.0
        
    @_('TOKEN_MINUS TOKEN_Y')
    def y_term(self, p):
        self.coefficents[p.lineno, 1] = -1.0
        
    @_('number TOKEN_Z')
    def z_term(self, p):
        self.coefficents[p.lineno, 2] = float(p.number)
        
    @_('TOKEN_SUM TOKEN_Z')
    def z_term(self, p):
        self.coefficents[p.lineno, 2] = 1.0
        
    @_('TOKEN_MINUS TOKEN_Z')
    def z_term(self, p):
        self.coefficents[p.lineno, 2] = -1.0
        
    @_('x_term y_term z_term TOKEN_IGUAL number')
    def equation(self, p):
        self.results[p.lineno] = float(p.number)
    
    @_('x_term z_term y_term TOKEN_IGUAL number')
    def equation(self, p):
        self.results[p.lineno] = float(p.number)
        
    @_('y_term x_term z_term TOKEN_IGUAL number')
    def equation(self, p):
        self.results[p.lineno] = float(p.number)
    
    @_('y_term z_term x_term TOKEN_IGUAL number')
    def equation(self, p):
        self.results[p.lineno] = float(p.number)
    
    @_('z_term x_term y_term TOKEN_IGUAL number')
    def equation(self, p):
        self.results[p.lineno] = float(p.number)
    
    @_('z_term y_term x_term TOKEN_IGUAL number')
    def equation(self, p):
        self.results[p.lineno] = float(p.number)
        
    @_('equation NEXT_EQUATION equation NEXT_EQUATION equation END_SYSTEM')
    def system(self, p):
        return linalg.solve(self.coefficients, self.results)

if __name__ == '__main__':
    lexer = ptLexer()
    parser = ptParser()
    text = "5x+3y-z=6 & 7.2x-8y+1.9z=6.2 & 13y-7.2x+z=4.2 #"
    solutions = parser.parse(lexer.tokenize(text))
    print(solutions)

    while True:
        try:
            text = input('Parsertongue > ')
            solutions = parser.parse(lexer.tokenize(text))
            print(solutions)
            #need code here to show solutions
        except EOFError:
            break