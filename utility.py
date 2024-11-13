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
