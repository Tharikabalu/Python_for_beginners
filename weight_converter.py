weight=int(input('Enter your weight:'))
choose=input('l or k:')
choice=choose.lower()

if choice=='l':
    weight_in_kg=weight*0.454
    print(f'You are {weight_in_kg} kg')
else:
    weight_in_pounds=weight/0.454
    print(f'You are {weight_in_pounds} pounds')


