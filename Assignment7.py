#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
PeopleSoft ID: 1378052
Assignment7
"""
# Do a linear search
linear_count = 0
binary_count = 0
def linear_search(password_list, password):
    global linear_count
    linear_count = 0
    for item in password_list:
        linear_count += 1
        if item == password:
            return True
    return False

# Do a binary search
def binary_search(password_list, password):
    global binary_count
    binary_count = 0
    low = 0 # The lowest index where the password could be
    high = len(password_list) - 1 # The highest index where the password could be
    while high >= low: # Keep going until they cross
        mid = (low + high)//2 # Find the middle index
        binary_count += 1
        if password_list[mid] == password: # Check out the password there
            return True # We got lucky and found it!
        elif password_list[mid] > password: # Is the password earlier in the list?
            high = mid - 1
        else: # Is the password later in the list?
            low = mid + 1
    # The while loop is finished here
    return False # We looked everywhere and didn't find it


passwords = []
#1.) Load the words into a list
file = open('passwords_short.txt')
for password in file.readlines():
    passwords.append(password.strip())


#2.) Sort the list
passwords.sort()
#print(passwords) # Just to see
file.close()
print("Reading password data ... Complete!")
while True:
    #3.) Get a word from the user
    my_password = input("Please enter the password to search for: ")

    #4.) Search (linear) for the word in the list
    if linear_search(passwords, my_password):
        print("Linear Search: Password found after {} tries".format(linear_count))
    else:
        print("Linear Search: Password NOT found after {} tries".format(linear_count) )
    #5.) Report if it is/isn't found

    #6.) Search (binary) for the word in the list
    if binary_search(passwords, my_password):
        print("Binary Search: Password found after {} tries".format(binary_count))
    else:
        print("Binary Search: Password NOT found after {} tries".format(binary_count))
        #7.) Report if it is/isn't found
        if linear_search(passwords, my_password):
            print("Password found! You should change your password! ")
            #8.) Repeat from getting a word (step 3)