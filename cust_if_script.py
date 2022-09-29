#!/usr/bin/env python3

"""Amazon Music | Peter Vasquez
    Creating my own if script"""

def main():

    message = 'Final grade for '

    student = input("what is the students name?")
    grade = int(input("What is the students test score?"))

    if grade >= 90:
        message = message + student +  ' is A.'
    
    elif grade >=80:
        message = message + student +  ' is B.'

    elif grade >= 70:
        message = message + student +  ' is C.'

    elif grade >= 60:
        message = message + student +  ' is D.'

    else: 
        message = message + student + ' is F'

    print(message)

main()
