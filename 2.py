def exc_func(input_list):
    new_list = [input_list[el] for el in range(1, len(input_list)) if input_list[el] > input_list[el - 1]]
    return new_list


num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(exc_func(num_list))
