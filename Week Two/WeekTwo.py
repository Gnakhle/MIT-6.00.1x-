# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:31:29 2017

@author: Gerald
"""

low = 0
high = 100


user_input = input("Please think of a number between 0 and 100!")
 
while True:
    guess = int((high+low)/2)
    print("Is your secret number "+str(guess)+"?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if response == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif response == 'l':
        low = guess
    elif response == 'h':
        high = guess
    else:
        print("Sorry I did not understand your input.")
        
        
        