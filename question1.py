'''
question1.py

Create functions that fulfill the below descriptions
in the comments and also pass the tests in 
test_question1.py.

See the README for the marking rubric.

'''


# Write a function that returns True.
def always_true():
    return True


# Write a function that adds 2 to an input number
# and returns the result.
def plus_two(input_number):
    return input_number+2


# Write a function that throws a ValueError when a
# negative number is input. Otherwise it returns
# the input number.
def negative_error(input_number):
    """THis function does neg error"""
    if input_number < 0:
        raise ValueError
    else:
        
        return input_number


# Write a function that takes no input and just returns
# the string 'spam'.
def spam():
    return 'spam'


# Write a function that takes an input and returns
# a list with that input repeated 3 times as 3 items
# in the list.
def repeat(input_item):
    return [input_item, input_item, input_item]
