input_list = [1,2,3,4,[5,6,7,[8,9]]]
def innermost_list(innermost):
    for x in innermost: #creats the loop
        if type(x) == list:# checks to see if the type of the item is a list
            return innermost_list(x) #makes the item the new list if it was a list
        else:
            continue
    return innermost
print(innermost_list(input_list))

