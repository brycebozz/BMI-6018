def innermost_list_plus1(argument_list):
    innermost_list = argument_list
    while True: #Infinite while loop wont stop unless it hits break
        innermost = False #You have to assume it is not innermost
        for x in innermost_list:
            if type(x) == list: #sees if the types match
                innermost_list = x #makes innermost_list current list found
                innermost = True #true put in so when it goes to line 10 it does not end the loop
                break
        if innermost == False: #breaks from while loop if out of values in list and if innermost is false if it got to this line and innermost was true while loop would begin again.
            break
    list_plus1 = []
    for x in innermost_list:
        list_plus1.append(x+1) #too add one to each element of list the each value in inner most list I felt it was easier to make a new list and append the values from the nnermost list and add them by one
    return list_plus1




