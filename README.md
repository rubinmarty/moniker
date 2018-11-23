# Moniker: Lambdas Made Simple

## Setup

Just clone the repo and begin your program with this line:

    from moniker import _

## Usage

Moniker simply provides a nicer syntax for quickly defining simple python functions.

    # "def" syntax
    def f(x):
        return 3 * x + 2
       
    # "lambda" syntax
    f = lambda x: 3 * x + 2
   
    # Moniker syntax
    f = 3 * _ + 2

Functions defined using Moniker work just like regular functions:

    >>> f = 3 * _ + 2
    >>> f(0)
    2
    >>> f(1)
    5
    
These functions have an easy to read string representation, for simple debugging:

    >>> f = 3 * _ + 2
    >>> f
    ((3 * _) + 2)
    
They can even be combined using mathematical operators:

    >>> f = _**2
    >>> g = 2 * _
    >>> h = 1
    >>> p = f + g + h
    >>> p(0)
    1
    >>> p(1)
    4
    >>> p(2)
    9
    
    >>> f = _ - 3
    >>> g = _ - 2
    >>> p = f * g
    >>> p(2)
    0
    >>> p(3)
    0
    >>> p(4)
    2
    
Moniker's utility really shines in situations where you want to write a function inline, like when using higher-order functions:

    >>> data = [12, 0, 5, 100, -4, 33, 86]
    >>> list(filter(_ % 2 == 0, data))
    [12, 0, 100, -4, 86]
    >>> list(map(_ * 10, data))
    [120, 0, 50, 1000, -40, 330, 860]
    >>> sorted(data, key=abs(_ - 50))
    [33, 86, 12, 5, 0, 100, -4]
    
Moniker has tons of cool features, so give it a try!

    >>> f = _[-1]
    >>> f([13, 4, 78])
    78

    >>> g = _ * 16 + "Batman!"
    >>> g("na ")
    'na na na na na na na na na na na na na na na na Batman!'
