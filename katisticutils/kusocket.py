import socket

class _ClientSocketRequests:
    def __init__(self, Port, Host):
        self.port = Port
        self.host = Host

    def contactServer(self, Data, Close = True):
        SocketC = False
        s = socket.socket()
        
        for x in range(5):
            try:
                s.connect((self.host, self.port))
                SocketC = True
                break
            except:
                pass

        if not SocketC:
            return "Could not connect to server!"

        InitResponseBytes = str(s.recv(4096), "utf-8")

        try:
            Buffer = int(InitResponseBytes)
        except:
            s.close()
            return "Recieved invalid bytes"

        InitResponse = str(s.recv(Buffer), "utf-8")

        if InitResponse == "OK.":
            byteLength = str(len(Data.encode('utf-8')))
            s.send(bytes(byteLength, "utf-8"))
            s.send(bytes(Data, "utf-8"))

            ResponseBytes = str(s.recv(4096), "utf-8")

            try:
                Buffer = int(ResponseBytes)
            except:
                s.close()
                return "Recieved invalid bytes"

            Response = str(s.recv(Buffer), "utf-8")
            
            if Close:
                s.close()
            return Response

        else:
            return "Server sent response: "+InitResponse

class _ServerSocketRequests:
    def __init__(self, Port, Host):
        s = socket.socket()
        s.bind((Host, Port))
        self.s = s

    def Listen(self, ConConn):
        self.s.listen(ConConn)

    def Send(self, s, Data, Close = True):
        if type(Data) != str:
            if type(Data) == int:
                Data = str(Data)
            else:
                print("socket.Send only accepts str or int data.")
                return

        Bytes = str(len(Data.encode("utf-8")))
        s.send(bytes(Bytes, "utf-8"))
        s.send(bytes(Data, "utf-8"))

        if Close:
            s.close()

    def Recv(self, s):
        Length = str(s.recv(4096), "utf-8")

        try:
            Length = int(Length)
        except:
            print("Recieved invalid bytes")
            return None

        Request = str(s.recv(Length), "utf-8")

        return Request ## Leaves client hanging for answer, next use s.Send to respond.

    def Accept(self):
        c, addr = self.s.accept()

        InitResponse = "OK."
        self.Send(c, InitResponse, Close = False)

        Request = self.Recv(c)

        return [c, addr, Request] # Socket, Address, Request

def ReqBasedClientSocket(Port, Host):
    return _ClientSocketRequests(Port, Host)

def ReqBasedServerSocket(Port, Host):
    return _ServerSocketRequests(Port, Host)
