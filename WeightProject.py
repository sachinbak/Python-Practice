weight = float(input(print('Enter your weight')))
print(" The mention weight is in (K) kg or (L) lbs ?")
check = input(print(" write 'K' if weight is in Kg and 'L'  if weight is in lbs."))

if check.upper() == 'K':
    converted = weight / 0.45
    print("The weight in lbs is " + str(converted ))
else:
    converted = weight * 0.45
    print("The weight in kg is " + str(converted))


