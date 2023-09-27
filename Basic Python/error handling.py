import os
import pathlib as path
import sys

#
# try:
#     age = int(input("enter your age"))
# except :
#     print("""
#     please inter a valid age
#     """,sys.exc_info())


# name = {
#     "name":"venzee",
#     "name2":"milla",
#     "name3":"mack"
# }
# try:
#     getvalue = input('enter key name')
#     print(name[getvalue])
# except KeyError:
#     print(sys.exc_info())
#     if sys.exc_info() =="KeyError":
#         print("invalid key")
#


club = {
    "club": "arsenal",
    "club1": "porto",
    "club3": "liverpool",
    "club4": "new castle"
}

try:
    getvalue = input("enter key club ")
    print(club[getvalue])
except KeyError:
    print(sys.exc_info())
    if sys.exc_info() == "KeyError":
        print("invalid key")
