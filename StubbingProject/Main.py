"""
Name: Stubbing Project
Created: 09/19/2020
Author: Christopher Lebovitz
Assignment: Using a self-selected programming language and menu display method create a stubbed code file and executable.
Requirements:
    1.Your menu shall contain at least 10 menu items
    2.Your menu shall contain an exit item selection
    3.Your menu shall contain an error response for invalid entry
    4.Your menu shall display a message indicating that an item is incomplete when selected
    5.Your menu shall be continuously displayed until the exit item is selected.
    6.The item selection method is up to the developer
    7.Provide a test results document showing the correct execution via output display captures.
"""

"""
Name: Choice
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: check the user input and make sure its within the accepted values, if it is then create a dictionary to map 
         cases to their functionality
"""


def Choice(selection):
    # check the user input and make sure its within the accepted values
    # if it is then create a dictionary to map cases to their functionality
    if selection < 0 or selection > 10:
        print("option is invalid please choose a different option")
    else:
        options = {
            1: 'not yet implemented',
            2: 'not yet implemented',
            3: 'not yet implemented',
            4: 'not yet implemented',
            5: 'not yet implemented',
            6: 'not yet implemented',
            7: 'not yet implemented',
            8: 'not yet implemented',
            9: 'not yet implemented',
            10: 'not yet implemented'
        }
        print(options.get(selection))



"""
Name: Choice
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to be used to print the menu
"""


def printMenu():
    # Print the menu to the user
    print("\twelcome to the Cafeteria please select a food Combo below. Enter -1 to exit")
    print("****All combos comes with fries and a drink. the garden salad comes with a drink****")
    print("1: Small Burger Combo \n2: Medium Burger Combo \n3: Large Burger Combo \n4: 3 Tender Combo \n"
          "5: 4 Tender Combo \n6: 5 Tender Combo \n7: Small Chicken Sandwich Combo \n8: Medium Chicken Sandwich Combo "
          "\n9: Large Chicken Sandwich Combo \n10: Garden Salad")


if __name__ == "__main__":
    # prompt the user for a selection
    printMenu()
    # read in the input as an integer and save it
    option = int(input())
    while option != -1:
        # call the Choice function and print the return
        Choice(option)
        # prompt the user for a selection
        printMenu()
        # read in the input as an integer and save it
        option = int(input())
