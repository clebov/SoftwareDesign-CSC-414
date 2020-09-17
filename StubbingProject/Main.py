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
        return options.get(selection)


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
        print(Choice(option))
        # prompt the user for a selection
        printMenu()
        # read in the input as an integer and save it
        option = int(input())
