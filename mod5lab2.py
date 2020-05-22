"""
CTEC 121
Eddy
moduel 5 lab 2
<assignment/lab description
"""

""" IPO template
Input(s): family names
Process: asks what each fmaily a question of two
Output: puts the name of each value in a function
"""


def verse(name):
    print(name, "finger,", name, "finger, where are you?")


def refrain():

    print("here i am, here i am, how do you do?")
    print()


def sinfamilysong():
    print()
    verse("daddy")
    refrain()
    verse("brother")
    refrain()
    verse("mother")
    refrain()
    verse("sister")
    refrain()
    verse("baby")
    refrain()


def main():
    sinfamilysong()


main()
