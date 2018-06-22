import socket
import math

class _ClientSocketRequests:
    def __init__(self, Port, Host):
        self.port = Port
        self.host = Host
    
    def contactServer(self, Data):
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
            return "Recieved invalid bytes!"
        
        InitResponse = str(s.recv(Buffer). "utf-8")
        
        if InitResponse == "OK.":
            byteLength = len(Data.encode("utf-8"))
            strByteLength = str(byteLength)
            
            Repeats = byteLength / 20480
            Repeats = math.ceil(Repeats)
            strRepeats = str(Repeats)
            
            RBytes = str(len(strRepeats.encode("utf-8")))
            s.send(bytes(RBytes, "utf-8"))
            s.send(bytes(strRepeats, "utf-8"))
            
            for x in range(Repeats):
                if byteLength < 20480:
                    s.send(bytes(byteLength, "utf-8"))
                    s.send(bytes(Data, "utf-8"))
                
                else:
                    sData = ""
                    while len(sData.encode("utf-8")) != 20480:
                        sData += Data[0]
                        del Data[0]
