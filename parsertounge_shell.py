from sly import Lexer
from sly import Parser

while True:
    text = input('Parsertongue > ')
    result, error = lexer.run(text)

    if error: print(error.as_string())
    else: print(result)

    """equation = []
    for i in range (0,3):
      x = str(input('Enter your equation: '))
      equation.append(x)
      
      print(f'Equation {i+1}: {equation[i]}')
      i +=1
    
    print(f'Your equations are here: {equation} ')"""
