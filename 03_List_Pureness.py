def best_list_pureness(numbers, K):
    best_pureness = 0
    best_rotation = 0

    for rotation in range(K + 1):
        current_pureness = sum(index * num for index, num in enumerate(numbers))

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation

        numbers.insert(0, numbers.pop())

    return f"Best pureness {best_pureness} after {best_rotation} rotations"

# # Тестови случаи
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)