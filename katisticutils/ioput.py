import sys

if sys.platform == "win32":
    from msvcrt import getch
else:
    from getch import getch

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

def Select(SL, removeAfterSelected = False):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    
    Selecting = 0
    Up = 38
    Down = 40
    Enter = 13
    Nul = "b'\\xff'"

    '''
    UP
    
    b'\xe0'
    b'H'
    
    DOWN
    
    b'\xe0'
    b'P'

    ENTER

    b'\r'
    '''

    Selected = False

    while not Selected:
        NewSL = ""
        for x in range(len(SL)):
            if x == Selecting:
                NewSL += " >> " + SL[x]
            else:
                NewSL += "    " + SL[x]

            if x != len(SL) - 1:
                NewSL += "\n"

        print(NewSL)
        
        while True:
            Key = getch()
            Key = str(Key)

            if Key == Up:
                if Selecting == len(SL) - 1:
                    Selecting = 0
                else:
                    Selecting += 1
                break

            elif Key == Down:
                if Selecting == 0:
                    Selecting = len(SL) - 1
                else:
                    Selecting -= 1
                break

            elif Key == Enter:
                Selected = True
                break

        if Selected:
            if removeAfterSelected:
                for x in range(len(SL)):
                    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
            break
        else:
            for x in range(len(SL)):
                print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

    return SL[Selecting]
