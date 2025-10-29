import math

def alpha_beta(index, depth, max_depth, alpha, beta, maximizingPlayer, values):
    if depth == max_depth:
        return values[index]

    if maximizingPlayer:
        v = float('-inf')
        for i in range(2):
            child_index = 2 * index + i
            v = max(v, alpha_beta(child_index, depth + 1, max_depth, alpha, beta, False, values))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = float('inf')
        for i in range(2):
            child_index = 2 * index + i
            v = min(v, alpha_beta(child_index, depth + 1, max_depth, alpha, beta, True, values))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v


# User input
n = int(input("Enter number of leaf nodes (power of 2): "))
values = []
for i in range(n):
    val = int(input(f"Enter utility value of leaf {i+1}: "))
    values.append(val)

# Determine tree depth
depth = int(math.log2(n))

# Build tree level-wise
tree = []
index = 0
for d in range(depth + 1):
    level_nodes = 2 ** d
    level = []
    for i in range(level_nodes):
        if d == depth:
            level.append(values[index])
            index += 1
        else:
            level.append(None)
    tree.append(level)

# Fill internal nodes with placeholder '?'
for d in range(depth - 1, -1, -1):
    for i in range(len(tree[d])):
        tree[d][i] = '?'

# Display tree structure
print("\nGame Tree (top = root):")
for level in tree:
    print(level)

# Perform alpha-beta pruning
best_value = alpha_beta(0, 0, depth, float('-inf'), float('inf'), True, values)

print("\nBest possible value for MAX at root:", best_value)
