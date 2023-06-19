# animal = input()
#
# if animal == 'dog':
#     animal = 'mammal'
#     print(animal)
# elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
#     animal = 'reptile'
#     print(animal)
# else:
#     animal = 'unknown'
#     print(animal)

animal = input()

animal_class = {
    'dog': 'mammal',
    'crocodile': 'reptile',
    'tortoise': 'reptile',
    'snake': 'reptile'
}

if animal in animal_class:
    print(animal_class[animal])
else:
    print('unknown')