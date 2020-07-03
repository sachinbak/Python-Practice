cart = [10, 20, 30]
total = 0
i=1
for price in cart:
    total += cart[i]
    i+1
print(f'Total cart price : {total}')

cart = [10, 20, 30]
total = 0
for price in cart:
    total += price
print(f'Total cart price : {total}')
