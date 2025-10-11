# -*- coding: utf-8 -*-
#%% the humble print statement
'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''

def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      print(f'the nested loop whe creating: {arg_2_sum} when it should be making: {arg1[arg1_index]+arg2[arg1_index]}')
      arg1[arg1_index]=arg_2_sum
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

#1b
def correct_add_function(arg1,arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index], arg2[arg1_index]])
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1
#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index], arg2[arg1_index]]) #2a its been updated to what was done in 1b.
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

#print(wrong_add_function(arg_str_1,arg_str_2))

#Problem 2b
def exception_add_function(arg1, arg2):
    try:
        for x in range(len(arg1)):
            if type(arg1[x]) is not type(arg1[0]): #The is not checks to see if the type of the very first value in the arg1 list is not equal to it. If not it goes it then raises a Type Error. Chose index 0 of arg 1 because everything needs to be the same type as one element in the list so it doesn't matter which element I choose.
                raise TypeError(f'Your input argument 1 at index {x} is not of the expected type of {type(arg1[x])}.') #makes it a type error which pushes it to the except and the string assigns it a message. Said index because index 2 is the third number in list felt it was more correct than element.
        for x in range(len(arg2)):
            if type(arg2[x]) is not type(arg1[0]):
                raise TypeError(f'Your input argument 2 at index {x} is not of the expected type of {type(arg1[x])}.')
        print(f"All inputs in arguments should work since they are all the same type of {type(arg1[0])}.") #prints message if everything works and states the type.
    except TypeError as error: #this makes it so when a type error is found the exception is called and it converts the type error raised into a variable so the string created
        print(error)
exception_add_function(arg_str_1,arg_str_2)
#Problem 2c
def correction_add_function(arg1, arg2):
    try:
        arg1_copy = arg1.copy() #these variables were made so that if the function called doesn't modify original values as specified in instructions
        arg2_copy = arg2.copy()
        function_result=wrong_add_function(arg1_copy, arg2_copy) #assigned the function to the variable function_variable to the function so it wouldnt activate the function when called so it wouldnt change the values which would happen if the function itself was called.
        if function_result is None:
            raise Exception
        else:
            return function_result
    except Exception:
        arg1_str = [str(x) for x in arg1] #This creates a new list using values in arg1 and changes all values to a string.
        arg2_str = [str(x) for x in arg2] #This creates a new list using values in arg2 and changes all values to a string.
        return wrong_add_function(arg1_str, arg2_str)
