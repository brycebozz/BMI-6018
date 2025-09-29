def filter_list(argument_list, filter):
    new_list = []
    while True:
        if filter in argument_list: #checking to see if filter is in list so it doesnt loop forever if it isn't found
            for x in argument_list: #if there is a filter it starts looping until it finds the filter
                if x == filter:
                    new_list.append(x) #need to have filter in the list according to instructions example
                    return new_list
                else:
                    new_list.append(x)
        else:
            return "Filter not found in list." #returns message telling that fileter is not in the lsit