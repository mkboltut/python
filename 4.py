def exc_func (input_list):
    new_list = [el for el in input_list if input_list.count(el) == 1]
    return new_list


num_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(exc_func(num_list))
