""" For testing my queue program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

import myqueue

print("\033[3;35;40m") # Just makes the text look cool

def main():
    """ The main function to test all of the funcitons in myqueue module """
    # Enqueue Test
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    solution = "True"
    solution_list = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 5]"
    print("TESTING ENQUEUE VALUES:\n\nShould be", solution
          + "\nAnd list should now be ", solution_list)
    print(myqueue.enqueue(list1, 5))
    print(list1)

    solution = "False"
    solution_list = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 5]"
    print("\nShould be", solution + "\nAnd list should now be ", solution_list)
    print(myqueue.enqueue(list1, 8))

    print("\n---------------------------------------\n")

    # Dequeue Test
    list2 = [5]
    solution = "5"
    solution_list = "[]"
    print("TESTING DEQUEUE VALUES:\n\nShould be", solution +
          "\nAnd list should now be ", solution_list)
    print(myqueue.dequeue(list2))
    print(list2)

    solution = "None"
    solution_list = "[]"
    print("\nShould be", solution + "\nAnd list should now be ", solution_list)
    print(myqueue.dequeue(list2))
    print(list2)

    print("\n---------------------------------------\n")

    # Peek Test

if __name__ == "__main__":
    main()
