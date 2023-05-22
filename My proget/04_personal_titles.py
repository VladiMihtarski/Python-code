age = float(input())
gender = input()
address_is = ''

if age >= 16 and gender == 'm':
    address_is = 'Mr.'
elif age < 16 and gender == 'm':
    address_is = 'Master'
elif age >= 16 and gender == 'f':
    address_is = 'Ms.'
elif age < 16 and gender == 'f':
    address_is = 'Miss'

print(address_is)
