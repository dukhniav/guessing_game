#!/usr/bin/env python

import numpy as np
import pdb

def welcome():
    print(' _   _                 _                  _____                     _             ')            
    print('| \ | |               | |                / ____|                   (_)            ')
    print('|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ ')
    print('| . ` | | | | \'_ ` _ \| \'_ \ / _ \ \'__| | | |_ | | | |/ _ \/ __/ __| | \'_ \ / _` |')
    print('| |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |')
    print('|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |')
    print('                                                                             __/ |')
    print('                                                                            |___/ ')

def beg_message():
    print('I am going to pick a number between 0 and 100\n')

def get_num():
    return np.random.randint(low=0, high=100)

def low(first):
    if first:
        print('\rToo LOW', end='')
    else: 
        print('\rToo LOW | ', end='')    

def high(first):
    #pdb.set_trace()
    if first:
        print('\rToo HIGH', end='')
    else:
        print('\rToo HIGH | ', end='')

def just_right():
    print('You got it! ', end='')

def print_guesses(guesses):
    print('So far: ', end='')
    for x in range(len(guesses)):
        print(guesses[x], end='')
        print(' ', end='')

def check(num, guess):
    if guess < num:
        return 1
    elif guess > num:
        return 2
    else:
        return 0

def main():
    welcome()
    beg_message()

    num = get_num()

    status = -1
    counter = 0
    guesses = []
    first_guess = True

    while status != 0:
        guess = input('\nEnter a number: ')
        
        try:
            guess = int(guess)
            guesses.append(guess)

            status = check(num, guess)

            if status == 0:
                just_right()
                print('It took you ' + str(counter) + ' tries! Can you do better?')
                exit
            else:
                if status == 1:
                    low(first_guess)
                else:
                    high(first_guess)

                if len(guesses) > 1:
                    print_guesses(guesses)
            first_guess = False
            counter = counter + 1

        except ValueError:
            print('Please enter a number', end='')

if __name__ == "__main__":
    main()
