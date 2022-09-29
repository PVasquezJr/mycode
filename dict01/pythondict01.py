#!/usr/bin/env python3

""" Amazon Music | PVasquez
    fun with Dictionaries! """

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1",
          "version": "1.2", "vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])

print("Fist test -  .get()")
print(switch.get("lynx"))

print("Second test - .get()")
print(switch.get("lynx","THE KEY IS ON ANOTHER CASTLE!"))

print("Third test - .get()")
print(switch.get("version"))

print("FOURTH TEST - .keys()")
print(switch.keys())

print("FIFTH TEST - .values()")
print(switch.values())

print( "SIXTH TEST - .pop()" )
switch.pop("version") # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

print( "SEVENTH TEST - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "EIGHTH TEST - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )

