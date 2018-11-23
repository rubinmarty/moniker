import operator

class Func:

    # Unary Operators

    def __abs__(self):
        return UnOpFunc(operator.abs, self)

    def __pos__(self):
        return UnOpFunc(operator.pos, self)

    def __neg__(self):
        return UnOpFunc(operator.neg, self)

    def __len__(self):
        raise RuntimeError("Length is not supported") 

    # Binary Math Operators

    def __add__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.add, other)

    def __radd__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.add, self)

    def __mul__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.mul, other)

    def __rmul__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.mul, self)

    def __sub__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.sub, other)

    def __rsub__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.sub, self) 

    def __div__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.div, other) 

    def __rdiv__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.div, self) 

    def __floordiv__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.floordiv, other) 

    def __rfloordiv__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.floordiv, self) 

    def __pow__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.pow, other)

    def __rpow__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.pow, self)

    def __mod__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.mod, other)

    def __rmod__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(other, operator.mod, self)

    # Logical Operators

    def __invert__(self):
        return UnOpFunc(operator.invert, self)

    def __and__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.and_, other)


    def __or__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.or_, other)

    def __xor__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.xor, other)

    # Comparisons

    def __lt__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.lt, other)

    def __gt__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.gt, other)

    def __le__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.le, other)

    def __ge__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.ge, other)

    def __eq__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.eq, other)

    def __ne__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.ne, other)

    # Other

    def __index__(self):
        raise RuntimeError("Indexing is not supported") 

    def __getitem__(self, other):
        other = ensure_lambda(other)
        return BinOpFunc(self, operator.getitem, other)

class Constant(Func):
    def __init__(self, value):
        self.value = value

    def __call__(self, arg):
        return self.value

    def __repr__(self):
        return str(self.value)


class Identity(Func):
    def __call__(self, arg):
        return arg

    def __repr__(self):
        return "_"

class UnOpFunc(Func):
    def __init__(self, operator, right):
        self.right = right
        self.operator = operator

    def __call__(self, arg):
        return self.operator(self.right(arg))

    def __repr__(self):
        if self.operator == operator.abs:
            return f"abs({self.right})"
        elif self.operator == len:
            return f"len({self.right})"
        else:
            return str(self.operator) + str(self.right)

class BinOpFunc(Func):
    def __init__(self, left, operator, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __call__(self, arg):
        return self.operator(self.left(arg), self.right(arg))

    def __repr__(self):
        if self.operator == operator.getitem:
            return str(self.left) + "[" + str(self.right) + "]"
        else:
            return "(" + str(self.left) + " " + binop_to_string(self.operator) + " " + str(self.right) + ")"

def ensure_lambda(value):
    if not callable(value):
        return Constant(value)
    return value

def binop_to_string(op):
    if op == operator.add:
        return "+"
    elif op == operator.mul:
        return "*"
    elif op == operator.sub or op == operator.neg:
        return "-"
    elif op == operator.lt:
        return "<"
    elif op == operator.le:
        return "<="
    elif op == operator.gt:
        return ">"
    elif op == operator.ge:
        return ">="
    elif op == operator.eq:
        return "=="
    elif op == operator.ne:
        return "!="
    elif op == operator.is_:
        return "is"
    elif op == operator.not_:
        return "not"
    elif op == operator.is_not:
        return "is not"
    elif op == operator.abs:
        return "abs"
    elif op == operator.and_:
        return "and"
    elif op == operator.floordiv:
        return "//"
    elif op == operator.inv or op == operator.invert:
        return "~"
    elif op == operator.mod:
        return "%"
    elif op == operator.pow:
        return "**"
    else:
        return "?"
    
_ = Identity()
