#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:35:28 2023

@author: marion
"""

#The system should create accounts based on the following rules:
#The filename will be called xx-nn-yy-zz where xx is the initials of the customer,
# an is the length of the total name (first name and last name, yy is the alphabetical position 
#of the first initial and zz is the alphabetical position of the second initial (
#(see table below)- together they make up the pin number


import string

#function to determine the position of each initial
def alphabetical_position(char):
    alphabet = string.ascii_uppercase
    return alphabet.index(char) + 1



def create_account_filename(first_name, last_name):
    # Get initials
    first_initial = first_name[0] #x
    last_initial = last_name[0] #x

    # Calculate length of the total name
    name_length = len(first_name) + len(last_name) #nn

    # Calculate alphabetical positions
    first_position = alphabetical_position(first_initial) #yy
    last_position = alphabetical_position(last_initial) #zz

    # Create the filename
    filename = f"{first_initial}{last_initial}-{name_length:02d}-{first_position:02d}-{last_position:02d}.txt"
    
    return filename


# test
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

account_filename = create_account_filename(first_name, last_name)
print("Result:", account_filename)

    