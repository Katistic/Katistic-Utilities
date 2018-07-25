def join(DL, Seperater = ""):
    if type(DL) != list:
        raise TypeError("KatisticUtils/manage.py: Expected variable "+str(list)+", got "+str(type(DL))+".")
        return # In case
    
    Repeat = 0
    StrDL = ""
    for x in DL:
        if Repeat != 0:
            StrDL += Seperater
        StrDL += str(x)
    
    return StrDL

def isInt(D):
    if type(D) == int:
        return True
    
    if type(D) != str:
        raise TypeError("KatisticUtils/manage.py: Expected variable "+str(str)+", got "+str(type(D))+".")
        return
    
    try:
        int(D)
        return True
    except:
        return False
