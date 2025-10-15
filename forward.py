def parse_predicate(expr):
    expr = expr.strip()
    if '=>' in expr:
        premise, conclusion = expr.split('=>')
        premises = [parse_predicate(p.strip()) for p in premise.split('&')]
        conclusion = parse_predicate(conclusion.strip())
        return (premises, conclusion)
    if '(' in expr and expr.endswith(')'):
        pred_name = expr[:expr.index('(')]
        args = expr[expr.index('(')+1:-1].split(',')
        args = tuple(arg.strip() for arg in args)
        return (pred_name,) + args
    return (expr,)

def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unifyvar(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unifyvar(y, x, theta)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for xi, yi in zip(x, y):
            theta = unify(xi, yi, theta)
            if theta is None:
                return None
        return theta
    else:
        return None

def unifyvar(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif isinstance(x, str) and x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def applysubstitution(expr, theta):
    if isinstance(expr, tuple):
        pred = expr[0]
        args = []
        for arg in expr[1:]:
            if arg in theta:
                args.append(theta[arg])
            else:
                args.append(arg)
        return (pred,) + tuple(args)
    return expr

def expr_to_str(expr):
    if isinstance(expr, tuple):
        if len(expr) == 1:
            return expr[0]
        return f"{expr[0]}({', '.join(expr[1:])})"
    return str(expr)

def folfc(KB, query):
    inferred = set()
    added = True
    KB_parsed = []
    for rule in KB:
        if '=>' in rule:
            premises, conclusion = parse_predicate(rule)
            KB_parsed.append((premises, conclusion))
        else:
            KB_parsed.append(parse_predicate(rule))
    query_parsed = parse_predicate(query)
    facts = [fact for fact in KB_parsed if not isinstance(fact, tuple) or (isinstance(fact, tuple) and not isinstance(fact[0], list))]
    rules = [fact for fact in KB_parsed if isinstance(fact, tuple) and isinstance(fact[0], list)]

    inferred_facts = set()
    while added:
        added = False
        for rule in rules:
            premises, conclusion = rule
            subs_list = [{}]
            for p in premises:
                new_subs_list = []
                for fact in facts + list(inferred_facts):
                    for theta in subs_list:
                        theta_new = unify(p, fact, dict(theta))
                        if theta_new is not None:
                            new_subs_list.append(theta_new)
                subs_list = new_subs_list
            for theta in subs_list:
                q = applysubstitution(conclusion, theta)
                q_str = expr_to_str(q)
                if q not in facts and q not in inferred_facts:
                    inferred_facts.add(q)
                    added = True
                    if unify(q, query_parsed) is not None:
                        print(f"Inferred: {q_str}")
                        return theta
        facts.extend(list(inferred_facts))
        inferred_facts.clear()
    return False

n = int(input("enter number of sentences in knowledge base: "))
KB = [input(f"enter sentence {i+1}: ") for i in range(n)]
query = input("enter query: ")
result = folfc(KB, query)
if result:
    print("Query entailed. Substitution:", result)
else:
    print("Query not entailed.")
