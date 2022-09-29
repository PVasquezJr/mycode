#!/usr/bin/env python3

"""Amazon Music | PVasquez
    if conditionals"""

def main():
    
    # create the string hostname
    hostname = input("What value should we set for hostname?")
    
    # test logic with the `if` statement
    # what to do if this statement is found to be true
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print ( "Hostname matches expected config")
    
    print ("Exiting the script")
main()
