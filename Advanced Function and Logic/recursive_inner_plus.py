input_list = [[[9,8],7,6,5],4,3,2,1]
def innermost_list(innermost): #innermost_list finds innermost list where as innermost argument is used to find the innermost list.
    new_list = []
    for x in innermost: #creats the loop
        if type(x) == list:# checks to see if the type of the item is a list
            return innermost_list(x) #returns back to the beginning thus making it recursive and it replaces the previous list with a new one since the new argument is x.

    for item in innermost:
        new_list.append(item+1)
    return new_list




