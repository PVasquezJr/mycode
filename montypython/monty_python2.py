#!/usr/bin/env python3

"""Amazon Music | PVasquez
    while looping with conditionals"""

def main():

    turn = 0

    while True:

        turn = turn + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')

        answer = input("Your guess--->")
        
        if answer.lower() == 'brian':
            print('Correct')
            break

        elif turn == 3:
            print("Sorry, the answer was Brian.")
            break

        else:
            print('Sorry. you suck!.... Try Again!')

main()

