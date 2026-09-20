'''
Problem statement: You're leading an expedition to a treasure island.
 You have a backpack that can hold a maximum weight capacity (W).
 You are also given a list of items, each with a specific weight and profit value.
 Your goal is to pick items in such a way that the total profit is maximized without
 exceeding the backpack’s weight capacity.

 '''


def max_profit_recursive(profit , weight , capacity , ind = 0):
    if ind == len(weight):
        return 0 

    elif weight[ind] > capacity:
        return max_profit_recursive(profit , weight , capacity , ind + 1)

    else:
        option1 = max_profit_recursive(profit , weight , capacity , ind + 1 )
        option2 = profit[ind] + max_profit_recursive(profit , weight , capacity - weight[ind] , ind + 1)
        result = max(option1 , option2)
    return result

profit = [3,8,2,6,8,9,4, 12 , 23,7]
weight = [2, 6,1,6,9 , 3,3,12,20, 8]
capacity = 40

print(max_profit_recursive(profit , weight , capacity , 0))