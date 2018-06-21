def Join(DL, Seperater = ""):
    if type(DL) != list:
        raise TypeError("Expected variable "+str(list)+", got "+str(type(DL))+".")
        return # In case
    
    Repeat = 0
    StrDL = ""
    for x in DL:
        if Repeat != 0:
            StrDL += Seperater
        StrDL += str(x)
    
    return StrDL
