def lerp(a, b, t):
    return a + t * (b - a)


def all_items_same(lst):
    return all(x == lst[0] for x in lst)


def same_for_end_length(series, length):
    return all_items_same(series[-length:])


def end_increasing_for_length(series, length):
    if length <= 0 or length > len(series):
        raise ValueError("Length must be positive and less than or equal to the length of the series.")
    last_elements = series[-length:]
    for i in range(1, len(last_elements)):
        if last_elements[i] <= last_elements[i - 1]:
            return False
    return True


def end_decreasing_for_length(series, length):
    if length <= 0 or length > len(series):
        raise ValueError("Length must be positive and less than or equal to the length of the series.")
    last_elements = series[-length:]
    for i in range(1, len(last_elements)):
        if last_elements[i] >= last_elements[i - 1]:
            return False
    return True

#
# test = [100, 97.813, 95.8545, 95.8525, 95.8151, 95.7577, 95.5245, 95.1613, 95.1861, 95.1852, 94.171, 93.4358, 92.787,
#         92.7578, 89.782, 89.7635]
# running_list = []
# l = 2
# for index, val in enumerate(test):
#     running_list.append(val)
#     if len(running_list) >= l:
#         if index == 8:
#             pass
#         print(str(index) + ": " + str(end_increasing_for_length(running_list, l)))
#     else:
#         print(str(index) + ": None")
