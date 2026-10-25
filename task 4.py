
def minimax(depth, index, maximizing, values,
            alpha, beta):
    if depth == 2:
        return values[index]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            value = minimax(depth + 1, index * 2 + i,
                            False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            value = minimax(depth + 1, index * 2 + i,
                            True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 2, 9]

result = minimax(0, 0, True, values,
                 float('-inf'), float('inf'))

print("Best possible value:", result)
