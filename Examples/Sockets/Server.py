import katisticutils as ku

s = ku.socket.ReqBasedServerSocket(5120, "127.0.0.1")
s.Listen(5)

while 1:
    sock, addr, req = s.Accept()

    print(req)
    s.Send(sock, "Hello!")
