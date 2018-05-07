import SocketServer


class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):

        print "123"

if __name__ == "__main__":
    HOST, PORT = "192.168.1.136", 2020
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)