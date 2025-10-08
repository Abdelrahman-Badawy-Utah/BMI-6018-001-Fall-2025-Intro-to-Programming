# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:13:53 2025

@author: El-Wattaneya
"""
#Question 1a

def wrong_add_function_debug(numbers):
   
    #Prints detailed debugging information to show where the loop error occurs.
    
    total = 0
    correct_answer = sum(numbers)

    for num in numbers:
        print("\n--- Inside Loop Iteration ---")
        print(f"The 'total' before the operation is: {total}")
        print(f"The current number from the list is: {num}")
        print("We are making an error in the loop on the next line!")

        #This replaces total instead of adding to it
        total = num

        print(f"The 'total' AFTER the operation is: {total}")
        print(f"The correct answer is supposed to be: {correct_answer}")

    return total


test_list = [10, 20, 70]
debug_result = wrong_add_function_debug(test_list)
answer_1a = debug_result





# Question 1b:
def correct_add_function(arg1, arg2):
    
    #Correctly adds each element of arg2 to the matching element of arg1.
  
    arg1_index = 0
    while arg1_index < len(arg1):
        arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
        arg1_index += 1
    return arg1

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]
print(correct_add_function(arg1, arg2))




#2.a, 2.b, 2.c – Updated numeric section and exception handling
def wrong_add_function(arg1, arg2):
    
    #The function takes in two lists of integers, then it adds all of arg2 to each item of arg1.
    
    #If the lists are lists of strings, concatenate them
    
    # numeric section (fixed from Question 1)
    if all(isinstance(i, int) for i in arg1) and all(isinstance(i, int) for i in arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
            arg1_index += 1
        return arg1
    
    # string section
    elif all(isinstance(i, str) for i in arg1) and all(isinstance(i, str) for i in arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index] = arg1[arg1_index] + arg_2_sum
            arg1_index += 1
        return arg1




#Question 2.b
def exception_add_function(arg1, arg2):
    
    #Adds or concatenates two lists while catching type errors.
    #Returns a clear message if input data types are mixed or invalid.
    
    try:
        # numeric section
        if all(isinstance(i, int) for i in arg1) and all(isinstance(i, int) for i in arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
                arg1_index += 1
            return arg1
        
        # string section
        elif all(isinstance(i, str) for i in arg1) and all(isinstance(i, str) for i in arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                    arg_2_sum += arg2_elements
                arg1[arg1_index] = arg1[arg1_index] + arg_2_sum
                arg1_index += 1
            return arg1
        
        # mixed types (error)
        else:
            for idx, val in enumerate(arg1):
                if not isinstance(val, (int, str)):
                    raise TypeError(f"Your input argument 1 at element {idx} is not of the expected type. Please change this and rerun.")
            for idx, val in enumerate(arg2):
                if not isinstance(val, (int, str)):
                    raise TypeError(f"Your input argument 2 at element {idx} is not of the expected type. Please change this and rerun.")
            raise TypeError("Your input contains a mix of strings and integers. Please make all elements the same type.")
    
    except TypeError as e:
        return str(e)
    
arg_str_1 = ['1','2','3']
arg_str_2 = ['1','1',1]

print(exception_add_function(arg_str_1, arg_str_2))




# Question 2.C
def correction_add_function(arg1, arg2):
    
    #Handles mixed-type input by converting all elements to strings 
    #so the function can still process correctly via the string section.
  
    try:
        # numeric section
        if all(isinstance(i, int) for i in arg1) and all(isinstance(i, int) for i in arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
                arg1_index += 1
            return arg1
        
        # string section
        elif all(isinstance(i, str) for i in arg1) and all(isinstance(i, str) for i in arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                    arg_2_sum += arg2_elements
                arg1[arg1_index] = arg1[arg1_index] + arg_2_sum
                arg1_index += 1
            return arg1
        
        # mixed types → fix automatically
        else:
            print("Mixed types detected — converting all elements to strings for processing.")
            arg1 = [str(x) for x in arg1]
            arg2 = [str(x) for x in arg2]
            return correction_add_function(arg1, arg2)
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
arg_str_1 = ['1','2','3']
arg_str_2 = ['1','1',1]

print(correction_add_function(arg_str_1, arg_str_2))