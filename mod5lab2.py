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
# code from class
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
"""
# making one for myself to practice

"""
def verse(name):
    print("hello ", name, ", im testing for mode")


def refrain():
    print("wonderfull weather were having today")
    print()


def sinfamilysong():
    print()
    verse("motha")
    refrain()
    verse("motha agian")
    refrain()
    verse("cuuuusin")
    refrain()
    verse("sister")
    refrain()
    verse("baby")
    refrain()


def main():
    sinfamilysong()


main()
"""
# make a code that marks a letter for an age range

""""
def agerange():
    I = 0-1
    C = 1-13
    T = 12-18
    A = 18
    U = unknown
"""


def age():
    print(input("what is your age? "))


def functions():
    if age < 2:
        return "I"
    elif age < 13:
        return "C"
    elif age < 18:
        return "T"
    elif age <= 125:
        return "A"
    else:
        return "unknown"


def main():
    print()
    print("your character is:", functions, "")
    functions()


main()
