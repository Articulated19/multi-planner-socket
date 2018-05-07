import SocketServer
import json
import subprocess
import os
import socket
import time

plannerpath = "./multi_planner.o"
env = dict(os.environ)


class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        data = json.loads(data.decode())
        processID = data["id"]

        if data["request_type"] == "get_path":
            path = getPath(data, processID)
            socket = self.request[1]
            socket.sendto(json.dumps(path), self.client_address)

        if data["request_type"] == "get_path":
            remove_x = data["remove_x"]
            remove_y = data["remove_y"]

            proc = subprocess.Popen([
                plannerpath,
                str(processID),
                str(remove_x),
                str(remove_y)],
                stdout=subprocess.PIPE, env=env)
            i = 0


def getPath(data, processID):
    path = []

    startx = data["startx"]
    starty = data["starty"]
    goalx = data["goalx"]
    goaly = data["goaly"]

    print processID
    print startx
    print starty
    print goalx
    print goaly

    proc = subprocess.Popen([
        plannerpath,
        str(processID),
        str(startx),
        str(starty),
        str(goalx),
        str(goaly)],
        stdout=subprocess.PIPE, env=env)
    i = 0

    while True:
        line = proc.stdout.readline()
        if (line == ""):
            break
        pt = line.split(',')
        path.append((float(pt[0]), float(pt[1])))
        i += 1

if __name__ == "__main__":
    HOST, PORT = "192.168.1.136", 2525
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()