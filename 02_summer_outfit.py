# degrees = int(input())
# time_of_day = input()
#
# outfit = ''
# shoes = ''
#
# if time_of_day == 'Morning':
#     if 10 <= degrees <= 18:
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif 18 < degrees <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     else:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
# elif time_of_day == 'Afternoon':
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < degrees <= 24:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     else:
#         outfit = 'Swim Suit'
#         shoes = 'Barefoot'
# elif time_of_day == 'Evening':
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# update

def get_outfit(degrees, time_of_day):
    outfits = {
        'Morning': {
 (10, 18): ('Sweatshirt', 'Sneakers'),
            (19, 24): ('Shirt', 'Moccasins'),
            (25, 42): ('T-Shirt', 'Sandals')
        },
        'Afternoon': {
            (10, 18): ('Shirt', 'Moccasins'),
            (19, 24): ('T-Shirt', 'Sandals'),
            (25, 42): ('Swim Suit', 'Barefoot')
        },
        'Evening': {
            (10, 42): ('Shirt', 'Moccasins')
        }
    }

    for temperature_range, outfit_and_shoes in outfits[time_of_day].items():
        if temperature_range[0] <= degrees <= temperature_range[1]:
            return outfit_and_shoes

temperature = int(input())
time_of_day = input()

outfit, shoes = get_outfit(temperature, time_of_day)

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
