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

def Clear(Lines = 1):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    for loop in range(Lines):
        print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    sys.stdout.write(CURSOR_UP_ONE + "\r")

def Lock():
    sys.stdout.flush()

def Select(SL, removeAfterSelected = True):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    Selecting = 0
    Entrance = "b'\\xe0'"
    Down = "b'H'"
    Up = "b'P'"
    Enter = "b'\\r'"
    Nul = "b'\\xff'"

    Selected = False

    while not Selected:
        NewSL = ""
        for x in range(len(SL)):
            if x == Selecting:
                NewSL += " >> " + SL[x]
            else:
                NewSL += "    " + SL[x]

            if x != len(SL) + 1:
                NewSL += "\n"

        print(NewSL)

        while True:
            Key = getch()
            Key = str(Key)

            if Key == Entrance:
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
                for x in range(len(SL) + 1):
                    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
                sys.stdout.write(CURSOR_UP_ONE + "\r")
            break
        else:
            for x in range(len(SL) + 1):
                print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
            sys.stdout.write(CURSOR_UP_ONE + "\r")

    return SL[Selecting]


def GetValidInput(t, disp, length=[]):
    while True:
        data = input(disp)

        if type(length) == int:
            if len(data) != length:
                continue

        elif type(length) == list:
            if len(length) == 0:
                pass
            elif len(length) == 1:
                if len(data) < length[0]:
                    continue
            elif len(length) == 2:
                if len(data) < length[0] or len(data) > length[1]:
                    continue

        try:
            data = t(data)
            return data
        except:
            continue
