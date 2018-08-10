import sys

_LastLength = 0

def Print(Item):
    global _LastLength
    
    Item = str(Item)

    while len(Item) < _LastLength:
        Item += " "

    _LastLength = len(Item)
    sys.stdout.write("\r")
    sys.stdout.write(Item)

def Input(Text = None):
    if Text == None:
        Data = input()
    else:
        Print(Text)
        Data = input()
    
    return Data

def Lock():
    sys.stdout.flush()
