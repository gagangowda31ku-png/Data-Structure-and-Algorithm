

def max_profit_dp(profit , weight , capacity):
    n = len(weight)

    table = [[0 for _ in range(n + 1)] for _ in range(capacity + 1)]

    for i in range(n):
        for c in range(1 , capacity +1):
            if weight[i] > c:
                table[i+1][c] = table[i][c]
            
            else:
                table[i+1][c] = max(table[i][c] , profit[i] + table[i][c - weight[i]])

    return table[-1][-1]

profit = [3,8,2,6,8,9,4, 12 , 23,7]
weight = [2, 6,1,6,9 , 3,3 , 12,20, 8]
capacity = 40

print(max_profit_dp(profit , weight , capacity))
