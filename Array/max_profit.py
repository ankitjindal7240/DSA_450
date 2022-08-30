import  sys
arr = [ 2, 30, 15, 10, 8, 25, 80 ]

first_buy=-sys.maxsize
first_sell=0
second_buy=-sys.maxsize
second_sell=0

for i in range(len(arr)):
    # variables showing net amound in hand
    first_buy=max(first_buy,-arr[i])                    # negative value after first buy
    first_sell=max(first_sell,first_buy+arr[i])         #either possitive or zero
    second_buy=max(second_buy,first_sell-arr[i])        # profit after first sell - currtnet price
    second_sell=max(second_sell,second_buy+arr[i])      # either greater or eual to first sell

print(second_sell)