import json
import threading

Queue = []
Using = False

def WriteToFile(File, Data, Type = "Normal"):
    if Using:
        try:
            File = open(File, "r")
            File.close()
        except Exception:
            raise "Could not find file "+File

        Queue.append([File, Data, Type])

def ReadFromFile(File, Type = "Normal"):
    if Using:
        while 1:
            if len(Queue) > 0:
                break

        if Type == "Normal":
            with open(File, "r") as FFile:
                Data = File.read()
        elif Type == "JSON":
            with open(File, "r") as FFile:
                Data = json.load(FFile)

        return Data

def RunQueue():
    while 1:
        if len(Queue) > 0:
            for x in Queue:
                if x[3] == "Normal":
                    with open(x[1], "w") as File:
                        File.write(x[2])
                elif x[3] == "JSON":
                    with open(x[1], "w") as File:
                        json.dump(x[2], File)

def Use():
    _QueueThread = threading.Thread(target = RunQueue)
    _QueueThread.start()
