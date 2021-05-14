import sly
from sly import Parser
from sly import Lexer
import numpy as np

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

class ptParser(Parser):
    # Check State
    debugfile = 'parser.txt'
    
    # Get the token list from the lexer (required)
    tokens = ptLexer.tokens
    
    precedence = (
       ('left', TOKEN_X, TOKEN_Y, TOKEN_Z),
       ('left', TOKEN_SUM, TOKEN_MINUS), 
       ('left', TOKEN_INT, TOKEN_PERIOD), )

    #Create numpy array to store coefficients/result
    def __init__(self):
        self.coefficients = np.zeros((3, 3))
        self.results = np.zeros((3,1))
        self.solutions = np.array([0])
        

    
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
    
    @_('x_term')
    def number(self, p):
        return p.x_term
    
    @_('y_term')
    def number(self, p):
        return p.y_term
    
    @_('z_term')
    def number(self, p):
        return p.z_term
    
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
        
    @_('x_term y_term z_term TOKEN_IGUAL number NEXT_EQUATION x_term y_term z_term TOKEN_IGUAL number NEXT_EQUATION x_term y_term z_term TOKEN_IGUAL number END_SYSTEM')
    def system(self, p):
        self.coefficients = np.array([[p.x_term0, p.y_term0, p.z_term0],
                                      [p.x_term1, p.y_term1, p.z_term1],
                                      [p.x_term2, p.y_term2, p.z_term2]])
        self.results = np.array([p.number0, p.number1, p.number2])
        #print(self.coefficients)
        #print(self.results)
        return p.END_SYSTEM
    
    @_('x_term y_term TOKEN_IGUAL number NEXT_EQUATION x_term y_term TOKEN_IGUAL number END_SYSTEM')
    def system(self, p):
        self.coefficients = np.array([[p.x_term0, p.y_term0],
                                      [p.x_term1, p.y_term1]])
        self.results = np.array([p.number0, p.number1])
        #print(self.coefficients)
        #print(self.results)
        return p.END_SYSTEM
        
    @_('system')
    def number(self, p):
        try:
            self.solutions = np.linalg.solve(self.coefficients, self.results)
        except np.linalg.LinAlgError:
            self.solutions = np.array([0])
        return (self.coefficients, self.results, self.solutions)

if __name__ == '__main__':
    lexer = ptLexer()
    parser = ptParser()
    
    while True:
         try:
            text = input('Parsertongue > ')
            output = parser.parse(lexer.tokenize(text))
            if type(output) is tuple:
                coefficients, results, solutions = output
                if solutions.size == 2:
                    print("Equation 1: (%r)x + (%r)y = %r" % (coefficients[0,0], coefficients[0,1], results[0]))
                    print("Equation 2: (%r)x + (%r)y = %r" % (coefficients[1,0], coefficients[1,1], results[1]))
                    print("Solutions:\n x = %r\n y = %r" % (solutions[0], solutions[1]))
                elif solutions.size == 3:
                    print("Equation 1: (%r)x + (%r)y + (%r)z = %r" % (coefficients[0,0], coefficients[0,1], coefficients[0,2], results[0]))
                    print("Equation 2: (%r)x + (%r)y + (%r)z = %r" % (coefficients[1,0], coefficients[1,1], coefficients[1,2], results[1]))
                    print("Equation 3: (%r)x + (%r)y + (%r)z = %r" % (coefficients[2,0], coefficients[2,1], coefficients[2,2], results[2]))
                    print("Solutions:\n x = %r\n y = %r\n z = %r" % (solutions[0], solutions[1], solutions[2]))
                else:
                    if results.size == 2:
                        print("Equation 1: (%r)x + (%r)y = %r" % (coefficients[0,0], coefficients[0,1], results[0]))
                        print("Equation 2: (%r)x + (%r)y = %r" % (coefficients[1,0], coefficients[1,1], results[1]))
                        print("ERROR OCCURRED, THIS SYSTEM OF EQUATIONS IS NOT SOLVABLE")
                    elif results.size == 3:
                        print("Equation 1: (%r)x + (%r)y + (%r)z = %r" % (coefficients[0,0], coefficients[0,1], coefficients[0,2], results[0]))
                        print("Equation 2: (%r)x + (%r)y + (%r)z = %r" % (coefficients[1,0], coefficients[1,1], coefficients[1,2], results[1]))
                        print("Equation 3: (%r)x + (%r)y + (%r)z = %r" % (coefficients[2,0], coefficients[2,1], coefficients[2,2], results[2]))
                        print("ERROR OCCURRED, THIS SYSTEM OF EQUATIONS IS NOT SOLVABLE")
            else:
                print(output)
        except EOFError:
            break
