import sly
from sly import Parser
from parsertounge_lexer import ptLexer
import numpy as np

class ptParser(Parser):
    # Check State
    debugfile = 'parser.txt'
    
    # Get the token list from the lexer (required)
    tokens = ptLexer.tokens
    
#    precedence = (
#       ('left', TOKEN_SUM, TOKEN_MINUS), 
#       ('left', TOKEN_INT, TOKEN_PERIOD),
#       ('left', TOKEN_X, TOKEN_Y, TOKEN_Z), )

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
        return p.number
        
    @_('TOKEN_SUM TOKEN_X')
    def x_term(self, p):
        return 1.0
        
    @_('TOKEN_MINUS TOKEN_X')
    def x_term(self, p):
        return -1.0
    
    @_('number TOKEN_Y')
    def y_term(self, p):
        return p.number
        
    @_('TOKEN_SUM TOKEN_Y')
    def y_term(self, p):
        return 1.0
        
    @_('TOKEN_MINUS TOKEN_Y')
    def y_term(self, p):
        return -1.0
        
    @_('number TOKEN_Z')
    def z_term(self, p):
        return p.number
        
    @_('TOKEN_SUM TOKEN_Z')
    def z_term(self, p):
        return 1.0
        
    @_('TOKEN_MINUS TOKEN_Z')
    def z_term(self, p):
        return -1.0
        
    @_('x_term y_term z_term TOKEN_IGUAL number')
    def equation(self, p):
        return np.array([p.x_term, p.y_term, p.z_term, p.number])
    
    @_('x_term z_term y_term TOKEN_IGUAL number')
    def equation(self, p):
        return np.array([p.x_term, p.y_term, p.z_term, p.number])
        
    @_('y_term x_term z_term TOKEN_IGUAL number')
    def equation(self, p):
        return np.array([p.x_term, p.y_term, p.z_term, p.number])
    
    @_('y_term z_term x_term TOKEN_IGUAL number')
    def equation(self, p):
        return np.array([p.x_term, p.y_term, p.z_term, p.number])
    
    @_('z_term x_term y_term TOKEN_IGUAL number')
    def equation(self, p):
        return np.array([p.x_term, p.y_term, p.z_term, p.number])
    
    @_('z_term y_term x_term TOKEN_IGUAL number')
    def equation(self, p):
        return np.array([p.x_term, p.y_term, p.z_term, p.number])
        
    @_('equation NEXT_EQUATION equation NEXT_EQUATION equation END_SYSTEM')
    def system(self, p):
        self.coefficients[0] = equation0[:3]
        self.coefficients[1] = equation1[:3]
        self.coefficients[2] = equation2[:3]
        self.results[0] = equation0[4]
        self.results[1] = equation1[4]
        self.results[0] = equation2[4]
        return END_SYSTEM
    
    #@_('END_SYSTEM')
    #def 

if __name__ == '__main__':
    lexer = ptLexer()
    parser = ptParser()
    #text = "5x+3y-z=6 & 7.2x-8y+1.9z=6.2 & 13y-7.2x+z=4.2 #"
    #solutions = parser.parse(lexer.tokenize(text))
    #print(solutions)
    
    while True:
        try:
            text = input('Parsertongue > ')
            solutions = parser.parse(lexer.tokenize(text))
            print(solutions)
            #need code here to show solutions
        except EOFError:
            break
