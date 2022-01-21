def fractionalKnapsack(W,n,items):
    curr_weight=0
    curr_val=0
    items=sorted(items,key= lambda x:(x.value/x.weight),reverse=True)
    for i in range(n):
        if curr_weight +items[i].weight<=W:
            curr_weight+=items[i].weight
            curr_val+=items[i].value
        else:
            fractinal_wt=W-curr_weight
            curr_val+=items[i].value * (fractinal_wt/items[i].weight)
            break
    return curr_val