## Introducing Parsertongue - Python Programming Language

## Project Description
`Parsertongue` is a Python Programming Language that was created for a class project and may or may not be used for other purposes. We came up with the name after learning about parsers and to give it some character we added the word "tongue" simbolizing language.
### Functionality
For now, `Parsertongue` is just a calculator that recognizes multivariable equations in the form of matrices. Later on, it can be used for more advanced programming jobs. 

The user inputs a multivariable equation in standar form, `Parsertongue` can recognize the x, y, & z values. Let it be a 2x2 matrix or a 3x3 matrix, this language can efficiently output your multivariable values in just seconds.

## Instalations
Now, in order for you to effectively enjoy using `Parsertongue` you must install a few things!

First things first, you must have your preferred `Python IDE` downloaded to your computer. 
If you do not have one already, you can download one of the following:
1. PyCharm
2. VisualStudioCode
3. Spyder (needs Anaconda to run)
4. Xcode (only for MacOS)

***There are also plenty of websites where you can run python programming without having to download a Python IDE.***

You also need to `install` a python library called `sly`. This will help us build our `Lexer` and `Parser`.

### Installing Sly
Once you download your `Python IDE`, go to your computer or app's terminal and copy the following command line:
> `pip install sly` 
> 
This will automatically download and install sly's latest version (sly 0.4) onto your computer so you can get started using `Parsertongue`.

Sly is a python library for writing parsers and compilers.

> If you'd like more info on the library `sly` click on SLY below.       
> More info on [SLY](https://sly.readthedocs.io/en/latest/sly.html).

### IMPORTANT Minor Language Inconveniences

> _`Parsertongue`_ _cannot recognize empty values!!_
> 
> Say we have the following equation as an input for a 3x3 matrix:
> 
> Example: 
> >Parsertongue > 2x + z = 4 & 3x - 2y + 3z = 4 & 7x - 7y + 9z = 8 #
> 
> This language cannot identify the missing _y_ in 2x + z = 2, it will simply read each token as it would normally read it and it would completey disregard the missiong variable.
> 
> BUT! There is a simple & quick fix to that problem! 
> 
> When inputing an equation with an empty value, simply write _0_ and the _empty variable_ you want.
> 
> Example: 
> >Parsertongue > 2x + _0y_ + z = 2 & 3x - 2y + 3z = 4 & 7x - 7y + 9z = 8 #
 


> _`Parsertongue`_ _cannot identify the values of said specific out of order variables!!_
> This language does not evaluate the equation properly if the user inputs a multivariable equation in a different order that is not from _x-z_.
> 
> Example: 
> 
> _User Input_
> >Parsertongue > 3x - 2z + 3y = 4
> >
> _Parsertongue Output_
> >Parsertongue > [3 -2 3][4]
> 
> Instead of:
> >Parsertongue > [3 3 -2][4]



#### Are you still unsure about how this language works?
##### Video Tutorial on How to use [`Parsertongue`](LINK).



