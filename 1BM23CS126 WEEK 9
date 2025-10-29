from itertools import combinations
def unify(x, y, subst):
    if subst is None:
        return None
    elif x == y:
        return subst
    elif isinstance(x, str) and x[0].islower():  # variable
        return unify_var(x, y, subst)
    elif isinstance(y, str) and y[0].islower():  # variable
        return unify_var(y, x, subst)
    elif isinstance(x, tuple) and isinstance(y, tuple) and x[0] == y[0] and len(x) == len(y):
        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    else:
        return None
def unify_var(var, x, subst):
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    else:
        new_subst = subst.copy()
        new_subst[var] = x
        return new_subst
def substitute(literal, subst):
    """Apply substitution to a literal"""
    return (literal[0],) + tuple(subst.get(a, a) for a in literal[1:])
def negate(literal):
    if literal[0].startswith('~'):
        return (literal[0][1:],)+literal[1:]
    else:
        return ('~'+literal[0],)+literal[1:]
def complementary(l1, l2):
    """Check if two literals are complementary"""
    return (l1[0] == '~' + l2[0]) or (l2[0] == '~' + l1[0])
def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if complementary(li, lj):
                subs = unify(li, negate(lj), {})
                if subs is not None:
                    new_ci = [substitute(l, subs) for l in ci if l != li]
                    new_cj = [substitute(l, subs) for l in cj if l != lj]
                    new_clause = list(set(new_ci + new_cj))
                    resolvents.append(tuple(sorted(new_clause)))
    return resolvents
def resolution(kb, query):
    clauses = [list(c) for c in kb] + [[negate(query)]]
    print("KNOWLEDGE BASE ")
    for i, c in enumerate(kb, 1):
        print(f"Clause {i}: {c}")
    print("\nQuery:", query)
    print("Initial Clauses:")
    for i, c in enumerate(clauses, 1):
        print(f"C{i}: {c}")
    print()
    step=1
    while True:
        new=[]
        for (ci, cj) in combinations(clauses, 2):
            resolvents=resolve(ci, cj)
            for res in resolvents:
                print(f"Step {step}: Resolving {ci} and {cj}")
                print(f"⟹{res}")
                step+=1
                if not res:
                    print("\n Empty clause derived. QUERY IS ENTAILED.")
                    return True
                if list(res) not in clauses and list(res) not in new:
                    new.append(list(res))
        if not new:
            print("\n No new clauses. QUERY IS NOT ENTAILED.")
            return False
        clauses.extend(new)
kb = [[('~human', 'x'), ('mortal', 'x')],
    [('human', 'socrates')]]
query = ('mortal', 'socrates')
resolution(kb, query)
