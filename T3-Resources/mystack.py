""" Stack program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

def push(stack, value):
    """ Adds value on top of stack """
    stack.append(value)

def pop(stack):
    """ Removes end value of stack and returns it """
    return_value = "None"
    if len(stack) > 0:
        return_value = stack[-1]
        del stack[-1]
    return return_value

def isempty(stack):
    """ Checks if the stack is empty """
    return_value = True
    if len(stack) > 0:
        return_value = False
    return return_value

def peek(stack):
    """ Returns the top value of the stack """
    return_value = "None"
    if len(stack) > 0:
        return_value = stack[-1]
    return return_value