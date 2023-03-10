# This program allows a user to choose an addition or subtraction problem
# generated by the computer
# 11-08-2021
# CTI-110 P5HW2 - Math Quiz
# James Atkins
#

import random

def add_random_numbers():
    computer_choice_one = random.randint(1,1000)
    computer_choice_two = random.randint(1,1000)
    computer_sum = (computer_choice_one + computer_choice_two)
    print(' ',computer_choice_one)
    print('+',end=' ')
    print(computer_choice_two)
    print('-----')
    print('Enter your answer.')
    answer = int(input())
    num_guesses = 1
    while (answer != computer_sum):
        print('That is incorrect. Try again.')
        answer = int(input())
        num_guesses = num_guesses + 1
    if (answer == computer_sum):
        print('Congradulations!!! That is correct')
        print('Number of guesses:',num_guesses)
        print('')
        display_menu()


def subtract_random_numbers():
    computer_choice_one = random.randint(1,1000)
    computer_choice_two = random.randint(1,1000)
    computer_sum = (computer_choice_one - computer_choice_two)
    print(' ',computer_choice_one)
    print('-', end=' ')
    print(computer_choice_two)
    print('-----')
    answer = int(input())
    print('Enter your answer.')
    num_guesses = 1
    while (answer != computer_sum):
        print('That is incorrect. Try again.')
        answer = int(input())
        num_guesses = num_guesses + 1
    if (answer == computer_sum):
        print('Congradulations!!! That is correct')
        print('Number of guesses:',num_guesses)
        print('')
        display_menu()
            

def display_menu():
    print('MAIN MENU')
    print('---------------------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('')
    print('Please choose one of the menu options:', end=' ')
    user_choice = int(input())
    if (user_choice == 1):
        add_random_numbers() 
    elif (user_choice == 2):
        subtract_random_numbers() 
    elif (user_choice == 3):
        print('Thanks for playing! Bye!!!')
        

display_menu()
