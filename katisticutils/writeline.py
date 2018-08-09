import sys

_LastLength = 0

def Write(Item):
    global _LastLength
    
    Item = str(Item)

    while len(Item) < _LastLength:
        Item += " "

    _LastLength = len(Item)
    sys.stdout.write("\r")
    sys.stdout.write(Item)
