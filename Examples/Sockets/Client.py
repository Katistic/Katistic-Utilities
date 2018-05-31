import katisticutils as ku

s = ku.socket.ReqBasedClientSocket(5120, "127.0.0.1")

while 1:
    Data = input("What would you like to send to the server? ")
    Resp = s.contactServer(Data)
    print("\n"*150)
    print("Server responded with "+Resp)
