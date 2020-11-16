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
import os
import time
import random
from collections import Counter

"""
Name: create_Options
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: create a dictionary to map cases to their functionality
"""


def create_Options():
    switch = {
        1: {"order": 'Small Burger Combo', "price": 8.99, "ticket": 'burger,small drink,small fry'},
        2: {"order": 'Medium Burger Combo', "price": 12.99, "ticket": 'burger,medium drink, medium fry'},
        3: {"order": 'Large Burger Combo', "price": 14.99, "ticket": 'burger, large drink, large fry'},
        4: {"order": '3 Tender Combo', "price": 6.99, "ticket": 'tender, small drink, small fry'},
        5: {"order": '4 Tender Combo', "price": 8.99, "ticket": 'tender, medium drink, medium fry'},
        6: {"order": '5 Tender Combo', "price": 9.99, "ticket": 'tender, large drink, large fry'},
        7: {"order": 'Small Chicken Sandwich Combo', "price": 5.99, "ticket": 'CkSand, small drink, small fry'},
        8: {"order": 'Medium Chicken Sandwich Combo', "price": 7.99, "ticket": 'CkSand, medium drink, medium fry'},
        9: {"order": 'Large Chicken Sandwich Combo', "price": 8.99, "ticket": 'CkSand, large drink, large fry'},
        10: {"order": 'Garden Salad', "price": 10.99, "ticket": 'salad, water, fruit'}
    }
    return switch


"""
Name: Choice
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: based off of the selection return a tuple of the data needed
"""


def choice(selection, combo):
    if int(selection) == 4 or int(selection) == 5 or int(selection) == 6 or int(selection) == 10:
        return combo.get(int(selection)).__getitem__('order'), combo.get(int(selection)).__getitem__(
            'price'), combo.get(int(selection)).__getitem__('ticket')  # return a tuple of the order, price, and ticket
    else:
        dress = input('how would you like this dressed? if nothing is entered it will be fully dressed'
                      ' (pickle, lettuce, tomato, onion): ')
        if dress == '':
            dress = 'no_Mod'
        print(dress)
        return combo.get(int(selection)).__getitem__('order'), combo.get(int(selection)).__getitem__(
            'price'), combo.get(int(selection)).__getitem__(
            'ticket'), 'dress: ' + dress  # return a tuple of the order, price, and ticket


"""
Name: PrintMenu
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to be used to print the menu
"""


def print_Menu():
    # Print the menu to the user
    print("\t\t****All combos comes with fries and a drink. the garden salad comes with a drink****\n")
    print("1: Small Burger Combo \n2: Medium Burger Combo \n3: Large Burger Combo \n4: 3 Tender Combo \n"
          "5: 4 Tender Combo \n6: 5 Tender Combo \n7: Small Chicken Sandwich Combo \n8: Medium Chicken Sandwich Combo "
          "\n9: Large Chicken Sandwich Combo \n10: Garden Salad")


"""
Name: print_Order
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to be used to display to the user what is in the cart.
"""


def print_Order(order):
    print()
    total = 0
    if len(order) == 0:  # if the orders list is empty tell the user
        print('There is nothing in the cart\n')
    else:  # else print the content of the list and give tax and total
        for x in order:  # for every order in the list
            print(x[0] + str(x[1]).rjust(37 - len(x[0]), ' '))
            total += x[1]
        tax = total * .07  # calculate the tax
        tax = round(tax, 2)  # round it to the nearest 2 decimal places
        total = tax + total  # add it to the total
        total = round(total, 2)  # round total to the nearest 2 decimal places
        print('----------------------------------------')
        print("Current Tax", str(tax).rjust(25, ' '))
        print("Current Total", str(total).rjust(23, ' '))


"""
Name: print_Order
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to be used to display to the user what is in the cart.
"""


def process_Receipt(order, number):
    if order:  # if the order list contains orders
        total = 0
        tax = 0
        f = open('receipt.txt', 'w')
        f.write("\t\tThank you!")
        f.write('\n\tYour order number is: ' + str(number))
        f.write('\nTransaction number' + str(round((random.random() * 10000))).rjust(10, ' '))
        f.write('\n\n')
        for x in orders:  # for every order in the list
            f.write(x[0] + str(x[1]).rjust(37 - len(x[0]), ' '))
            f.write('\n')
            total += x[1]
        f.write('----------------------------------------\n')
        f.write('Subtotal' + str(total).rjust(29, ' '))
        f.write('\n')
        tax = total * .07  # calculate the tax
        tax = round(tax, 2)  # round it to the nearest 2 decimal places
        f.write('Tax' + str(tax).rjust(34, ' '))
        f.write('\n')
        total = tax + total  # add it to the total
        total = round(total, 2)  # round total to the nearest 2 decimal places
        f.write('Total' + str(total).rjust(32, ' '))

        pay(total, order, f)  # call the pay function to process the payment


"""
Name: send_ticket
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to create the ticket that is sent to the kitchen.
"""


def send_Ticket(order):
    f = open('ticket.txt', 'w')
    temp = ()  # create a temp tuple to store each individual tuple in the order list
    for item in order:
        temp += tuple(item[2].split(','))  # add 2nd element of each tuple to the temp tuple
    temp2 = Counter(tuple(temp))  # count the occurrence of every value in the temp tuple
    for value, count in temp2.most_common():
        f.write(str(count) + 'x ' + value + '\n')  # output the value and the count to the ticket
    f.write('!!!!Sandwich mod!!!!\n')  # notify that there sandwiches and show if there is a mod or not
    for thing in order:
        if len(thing) == 4:
            f.write(str(order.index(thing) + 1) + ' ' + thing[0] + ' ' + thing[3] + '\n')

    f.close()
    os.startfile('ticket.txt')


"""
Name: clear
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to clear the screen. works on unix and windows machines
"""


def clear():
    # if windows
    if os.name == 'nt':
        _ = os.system('cls')
    # if unix
    else:
        _ = os.system('clear')


"""
Name: pay
Created: 09/18/2020
Author: Christopher Lebovitz
Purpose: function to process the payment receded by the customer (cash  only)
"""


def pay(total, order, f):

    print('Your total is: ' + str(total))  # give the total to the customer
    payment = input('please enter payment amount: ')  # prompt for payment
    if payment.isdecimal() and float(payment) < 1000:
        payment = round(float(payment), 2)  # round payment to the nearest 2 decimal places
        while total > 0:  # while the total is greater than 0
            if payment > total:  # if they payment is larger than total
                payment = payment - total  # calculate the change
                print('Change: ', round(payment, 2))  # output change
                break  # break loop since the payment is over amount due
            elif total == 0:  # if total is 0 the amount due has been paid.
                break
            elif payment == total:  # if payment == total then exact amount has been received
                break
            else:  # else the payment is less than the total. keep asking for payment until one of the other conditions is meet
                total = total - payment
                total = round(total, 2)  # round total to the nearest 2 decimal places
                payment += round(payment, 2)
                print('Amount due: ' + str(total))
                payment = round(float(input('please enter payment amount: ')), 2)

        send_Ticket(order)  # call the sent_ticket function to send the order to the kitchen
        f.write('\n----------------------------------------')
        f.write('\nPayment' + str(round(payment, 2)).rjust(30, ' '))
        os.startfile('receipt.txt')
        f.close()
        order.clear()
    else:
        print('Input Error please begin transaction again.')


if __name__ == "__main__":
    # prompt the user for a selection
    orders = []
    order_Num = 1
    # take in user input

    # create dictionary that holds the choices
    options = create_Options()

    while True:
        # clear screen
        clear()
        print(
            "Welcome to the Cafeteria please select a food Combo below. type exit to quit program,"
            " c for cart, and cancel to cancel order")
        print_Menu()
        # take in user input and covert it to lower string
        option = input().lower()
        # validate input and call the appropriate input
        # if user enters c prent options selected and ask if they would like to check out
        if option == '':  # if user presses enter without any input don't evaluate the rest and loop again
            continue
        elif option == 'c':
            print_Order(orders)
            x = input('Would you like to check out? yes or no?\n')  # if yes call process_Receipt
            if x == 'yes' or x == 'y':
                process_Receipt(orders, order_Num)
                order_Num += 1  # increase order number for next customer
                orders.clear()  # clear the orders list
        elif option == 'cancel' and len(orders) != 0:  # verify that the current customer wants to cancel order
            cancel = input('Cancel order? y or no? ')  # read in input
            if cancel == 'y':  # if yes clear order
                orders.clear()
        elif option == 'exit':  # if exit is entered quit the program
            break
        elif option == 'r':  # if r is entered call process_Receipt, increment order number, and clear the order list
            if orders:
                process_Receipt(orders, order_Num)
                order_Num += 1
            else:
                print('Nothing is ordered')
        elif option.isdigit():
            if 1 <= int(option) <= 10:  # validate that the user enters the correct choice number
                orders.append(choice(option, options))
            else:
                print("option is invalid please choose a different option")
        else:  # if user enters anything other than the acceptable input print an error and ask for input again
            print("option is invalid please choose a different option")
        time.sleep(1)

        # prompt the user for a selection
