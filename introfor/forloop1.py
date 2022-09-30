#!/usr/bin/env python3

"""Amazon Music | PVasquez
    basic for loops"""

def main():
    # create the list called vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

    # create a second list of strings
    approved_vendors = ["cisco", "juniper", "big_ip"]

    # loop across the list called vendors
    for x in vendors:
        print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
        if x not in approved_vendors:   # if x does not appear within the list approved_vendors
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.")

main()
