def filter_list(argument_list, filter):
    new_list = []
    while True:
        for x in argument_list:
            if x == filter:
                new_list.append(x)
                return new_list
            else:
                new_list.append(x)


test = [1,2,3,4,5,6,7,8,9]
print(filter_list(test,6))