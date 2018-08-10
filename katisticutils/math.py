import math

def GetFactorsOf(Num):
    if type(Num) != int:
        raise TypeError("KatisticUtils/math.py: Expected type " + str(int) + ", got type " + type(Num))
    
    if not isWhole(Num):
        raise Exception("KatisticUtils/math.py: Number must be whole.")
    
    Factors = [1, Num]
    MaxFactor = math.ceil(Num / 2)
    
    for x in range(2, MaxFactor):
        if x in Factors: continue
        Ans = Num / x
        if isWhole(Ans):
            print("Found Factors:")
            print(int(Ans))
            print(int(x))
            if not int(x) in Factors: Factors.append(int(x))
            if not int(Ans) in Factors: Factors.append(int(Ans))
    
    return Factors

def IsWhole(Num):
    if Num % 1 == 0:
        return True
    else:
        return False
