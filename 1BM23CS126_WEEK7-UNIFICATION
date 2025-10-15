def isvariable(x):
    return isinstance(x,str) and x.islower()
def parseterm(expr):
    expr=expr.strip()
    if '(' in expr and expr.endswith(')'):
        func=expr[:expr.index('(')].strip()
        argsstr=expr[expr.index('(')+1:-1]
        args=[arg.strip() for arg in argsstr.split(',')]
        return (func,*args)
    else:
        return expr
def unify(x,y,theta=None):
    if theta is None:
        theta = {}
    if x==y:
        return theta
    elif isvariable(x):
        return unifyvar(x,y,theta)
    elif isvariable(y):
        return unifyvar(y,x,theta)
    elif isinstance(x,tuple) and isinstance(y,tuple) and len(x)==len(y):
        for xi,yi in zip(x,y):
            theta=unify(xi,yi,theta)
            if theta is None:
                return None
        return theta
    else:
        return None
def unifyvar(var,x,theta):
    if var in theta:
        return unify(theta[var],x,theta)
    elif x in theta:
        return unify(var,theta[x],theta)
    else:
        theta[var]=x
        return theta
expr1=input("enter 1st expression: ")
expr2=input("enter 2nd expression: ")
term1=parseterm(expr1)
term2=parseterm(expr2)
result=unify(term1,term2)
if result is None:
    print("cant unify")
else:
    print("Substitution:",result)
