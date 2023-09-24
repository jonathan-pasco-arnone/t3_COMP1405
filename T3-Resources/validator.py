""" Validation program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

import mystack

def isvalid(string):
    """ Checks if the parenthesis are valid """
    # Will keep track of the bracket openings in order
    bracket_openings = []
    return_value = True
    for item in string:
        # Checks if the character is an open bracket
        # If yes then it will record it on the stack
        if item == "(" or item == "[" or item == "{":
            mystack.push(bracket_openings,(item))

        # Checks if the character is each of the closing bracket types
        # If yes then it checks if the previous open bracket was the same type
        # If yes again then it will take the opening bracket out of the stack
        elif item == ")":
            if mystack.peek(bracket_openings) == "(":
                mystack.pop(bracket_openings)
            else:
                return_value = False
                break
        elif item == "]":
            if mystack.peek(bracket_openings) == "[":
                mystack.pop(bracket_openings)
            else:
                return_value = False
                break
        elif item == "}":
            if mystack.peek(bracket_openings) == "{":
                mystack.pop(bracket_openings)
            else:
                return_value = False
                break

    # If all the brackets were satisfied then the stack should be empty at the end
    # Unless there is a bracket that opens without any closing bracket
    if not mystack.isempty(bracket_openings):
        return_value = False
    return return_value
