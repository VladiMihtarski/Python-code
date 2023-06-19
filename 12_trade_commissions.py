town = input()
sales_volume = float(input())
commission = ''

if town == 'Sofia' and 0 <= sales_volume <= 500:
    commission = sales_volume * 0.05
elif town == 'Sofia' and 500 < sales_volume <= 1000:
    commission = sales_volume * 0.07
elif town == 'Sofia' and 1000 < sales_volume <= 10000:
    commission = sales_volume * 0.08
elif town == 'Sofia' and sales_volume > 10000:
    commission = sales_volume * 0.12
elif town == 'Varna' and 0 <= sales_volume <= 500:
    commission = sales_volume * 0.045
elif town == 'Varna' and 500 < sales_volume <= 1000:
    commission = sales_volume * 0.075
elif town == 'Varna' and 1000 < sales_volume <= 10000:
    commission = sales_volume * 0.10
elif town == 'Varna' and sales_volume > 10000:
    commission = sales_volume * 0.13
elif town == 'Plovdiv' and 0 <= sales_volume <= 500:
    commission = sales_volume * 0.055
elif town == 'Plovdiv' and 500 < sales_volume <= 1000:
    commission = sales_volume * 0.08
elif town == 'Plovdiv' and 1000 < sales_volume <= 10000:
    commission = sales_volume * 0.12
elif town == 'Plovdiv' and sales_volume > 10000:
    commission = sales_volume * 0.145
else:
    print("error")

if commission != '':
    formatted_commission = "{:.2f}".format(commission)
    print(formatted_commission)

    # dictionary
    town = input()
    sales_volume = float(input())

    commissions = {
        'Sofia': {
            (0, 500): 0.05,
            (500, 1000): 0.07,
            (1000, 10000): 0.08,
            (10000, float('inf')): 0.12
        },
        'Varna': {
            (0, 500): 0.045,
            (500, 1000): 0.075,
            (1000, 10000): 0.10,
            (10000, float('inf')): 0.13
        },
        'Plovdiv': {
            (0, 500): 0.055,
            (500, 1000): 0.08,
            (1000, 10000): 0.12,
            (10000, float('inf')): 0.145
        }
    }

    commission = None

    if town in commissions:
        for volume_range, rate in commissions[town].items():
            if volume_range[0] <= sales_volume <= volume_range[1]:
                commission = sales_volume * rate
                break

    if commission is not None:
        formatted_commission = "{:.2f}".format(commission)
        print(formatted_commission)
    else:
        print("Error")

# functions

def calculate_commission(town, sales_volume):
    commissions = {
        'Sofia': {
            (0, 500): 0.05,
            (500, 1000): 0.07,
            (1000, 10000): 0.08,
            (10000, float('inf')): 0.12
        },
        'Varna': {
            (0, 500): 0.045,
            (500, 1000): 0.075,
            (1000, 10000): 0.10,
            (10000, float('inf')): 0.13
        },
        'Plovdiv': {
            (0, 500): 0.055,
            (500, 1000): 0.08,
            (1000, 10000): 0.12,
            (10000, float('inf')): 0.145
        }
    }

    if town in commissions:
        for volume_range, rate in commissions[town].items():
            if volume_range[0] <= sales_volume <= volume_range[1]:
                return sales_volume * rate

    return None


def format_commission(commission):
    if commission is not None:
        return "{:.2f}".format(commission)
    else:
        return "Error"


town = input()
sales_volume = float(input())

commission = calculate_commission(town, sales_volume)
formatted_commission = format_commission(commission)

print(formatted_commission)
