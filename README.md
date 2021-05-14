## Introducing Parsertongue - Python Programming Language

## Project Description
`Parsertongue` is a Python based Programming Language that was created for a class project and may or may not be used for other purposes. The name was inspired after learning about parsers in class and by the fictional language to talk to snakes in the Harry Potter series, Parseltongue (relevant since the language is coded in Python).
### Functionality
For now, `Parsertongue` is just a calculator that recognizes multivariable systems of equations writen in plain text and solve them. Later on, it can be used for more advanced programming jobs. 

The user inputs a multivariable equation in standard form, `Parsertongue` can recognize the x, y, & z values. Whether it is a linear system of 2 or 3 variables, this language can efficiently output your solutions in a fraction of a second.

## Installations
Now, in order for you to effectively enjoy using `Parsertongue` you must install a few things!

First things first, you must have your preferred `Python IDE` downloaded to your computer. 
If you do not have one already, you can download one of the following:
1. PyCharm
2. VisualStudioCode
3. Spyder (needs Anaconda to run)
4. Xcode (only for MacOS)

***There are also plenty of websites where you can run python programming without having to download a Python IDE.***

You also need to `install` two python libraries:
1. `numpy` - this will help us with the actual math
2. `sly` - this will help us build our `Lexer` and `Parser`.

### Installing Libraries
Once you download your `Python IDE`, go to your computer or app's terminal and copy the following command line:
- NumPy:
```
pip install numpy
```
> More info on [NumPy](https://numpy.org).
> 
- SLY:
```
pip install sly
```
> More info on [SLY](https://sly.readthedocs.io/en/latest/sly.html).

- Note: some IDE's require `pip3` or `conda` instead of `pip`.

## Basic Writing Rules
Once you install everything, you are now ready to use this language.
When writing a system of 2 or 3 equations, after each equation you must seperate them by using `&` key.
When you are finished writing your 2 or 3 equations, end the system by using `#` key.

### IMPORTANT Minor Language Inconveniences
#### Minor Inconvenience #1
_`Parsertongue`_ _cannot recognize empty values!!_
 
Say we have the following equation as an input for a 3x3 matrix: 

Example: 
```
Parsertongue > 2x + z = 4 & 3x - 2y + 3z = 4 & 7x - 7y + 9z = 8 #
```
This language cannot identify the missing _y_ in 2x + z = 2, it will result in a syntax error.

BUT! There is a simple & quick fix to that problem! 

When inputing an equation with an empty value, simply write _0_ and the _empty variable_ you want.

Example: 
```
Parsertongue > 2x + 0y + z = 2 & 3x - 2y + 3z = 4 & 7x - 7y + 9z = 8 #
```

#### Minor Inconvenience #2
_`Parsertongue`_ _cannot identify the values of said specific out of order variables!!_
This language does not evaluate the equation properly if the user inputs a multivariable equation in a different order that is not from _x-z_.
 
Example: 

_User Input_
```
Parsertongue > 3x - 2z + 3y = 4 & 2x + y + z = 5.2 & -x + 9y - 4.2z = 8 #
```
Would give a syntax error because the first equation is out of order. Instead, we need:

_User Input_
```
Parsertongue > 3x + 3y - 2z = 4 & 2x + y + z = 5.2 & -x + 9y - 4.2z = 8 #
```
_Parsertongue Output_
```
Equation 1: (3.0)x + (3.0)y + (-2.0)z = 4.0
Equation 2: (2.0)x + (1.0)y + (1.0)z = 5.2
Equation 3: (-1.0)x + (9.0)y + (-4.2)z = 8.0
 
Solutions:
x = 0.7379061371841154
y = 1.846931407942239
z = 1.8772563176895314
```

#### Minor Inconvenience #3
_`Parsertongue`_ _requires the leading variable x in each equation to have an attached coefficient or operator_
 
If x does not have a leading coefficicent or operator (+ or -), it will result in a syntax error.

Example: 

_User Input_
```
Parsertongue > 3x + 3y - 2z = 4 & x + y + z = 5.2 & -x + 9y - 4.2z = 8 #
```
Would give a syntax error because x does not have a leading coefficient or operator. Instead, we need:

_User Input_
```
Parsertongue > 3x + 3y - 2z = 4 & +x + y + z = 5.2 & -x + 9y - 4.2z = 8 #
```
Or alternatively:

_User Input_
```
Parsertongue > 3x + 3y - 2z = 4 & 1x + y + z = 5.2 & -x + 9y - 4.2z = 8 # 
```
Both cases would give the following output:

_Parsertongue Output_
```
Equation 1: (3.0)x + (3.0)y + (-2.0)z = 4.0
Equation 2: (1.0)x + (1.0)y + (1.0)z = 5.2
Equation 3: (-1.0)x + (9.0)y + (-4.2)z = 8.0

Solutions:
x = 0.8176
y = 2.0624000000000002
z = 2.3200000000000003
```

## UNSOLVABLE EXAMPLES
Like any real matrix there can never be a system of equations where only one variable has 2 to 3 inputs. In a system of equations you must have at least one value for each variable. If the needs aren't met, then the result will be an error message stating it is unsolvable.

Here are some examples that will result in `ERROR MESSAGES`:
```
Parsertongue > 4x+0y=4 & 5x+0y=3 #
Equation 1: (4)x + (0)y = 4
Equation 2: (5)x + (0)y = 3
ERROR OCCURRED, THIS SYSTEM OF EQUATIONS IS NOT SOLVABLE

Parsertongue > 5x-3y+0z = 1 & -x + 1.2y -0z = -2.4 & 8.6x - 69y +0z = 32#
Equation 1: (5.0)x + (-3.0)y + (0.0)z = 1.0
Equation 2: (-1.0)x + (1.2)y + (0.0)z = -2.4
Equation 3: (8.6)x + (-69.0)y + (0.0)z = 32.0
ERROR OCCURRED, THIS SYSTEM OF EQUATIONS IS NOT SOLVABLE
```

## Are you still unsure about how this language works?
##### Video Tutorial on How to use [`Parsertongue`](https://youtu.be/cbaGi7vo26o).

