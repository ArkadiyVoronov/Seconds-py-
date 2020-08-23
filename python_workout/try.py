try:
    n = float(input('Enter a number: '))
    print(f'n = {n}')
except ValueError as e:
    print('Hey! That's not a valid number!')
