""" Queue program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

MAX_QUEUE_SIZE = 10

def enqueue(queue, value):
    """ Adds value to end of list unless at max """
    return_value = False
    if len(queue) < MAX_QUEUE_SIZE:
        queue.append(value)
        return_value = True
    return return_value

def dequeue(queue):
    """ Removes first value of list unless list is empty """
    return_value = "None"
    if len(queue) > 0:
        return_value = queue[0]
        del queue[0]
    return return_value

def peek(queue):
    """ Returns the first value of queue """
    return_value = "None"
    if len(queue) > 0:
        return_value = queue[0]
    return return_value

def isempty(queue):
    """ Checks if the queue is empty """
    return_value = True
    if len(queue) > 0:
        return_value = False
    return return_value

def multienqueue(queue, items):
    """ Adds as many of the items provided as possible to the queue """
    elements_added = 0 # Counts the amount of elements added
    for value in items:
        if enqueue(queue, value):
            elements_added += 1
        else:
            break
    return elements_added

def multidequeue(queue, number):
    """ Removes as many variables from the queue as
    possible up to the number provided """
    removed_items = []
    # Run until the number is completed
    while number > 0:
        removed_value = dequeue(queue)
        if removed_value == "None":
            break
        removed_items.append(removed_value)
        number -= 1
    return removed_items
