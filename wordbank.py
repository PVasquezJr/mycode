#!/usr/bin/env python3

import random

def main():

    #create wordbank list
    wordbank= ["indentation", "spaces"]
 
    tlgstudents= ["Aaron", "Andy", "Asif", 
                  "Brent", "Cedric", "Chris", 
                  "Cory", "Ebrima", "Franco", 
                  "Greg", "Hoon", "Joey", 
                  "Jordan", "JC", "LB", 
                  "Mabel", "Shon", "Pat", "Zach"]

    print(tlgstudents)
    wordbank.append(4)
    print(wordbank)

    choice= int(input("Pick a student number between 0 to 18!: "))-1
    student_name= tlgstudents[choice]

    print(f"Your picked name is {student_name}!")
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.") 

    student_name = random.choice(tlgstudents)
    print(f"{student_name}")

main()   
