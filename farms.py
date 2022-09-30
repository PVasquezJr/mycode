#!/usr/bin/env python3
"""Amazon Music | PVasquez
    Farm Challenge"""

def main():
    #create a dictionary list
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for x in farms:
        print(x.get("name"), end=":\n")

        for z in x.get("agriculture"):
            print(" -", z)

main()
