from xmlrpc.server import SimpleXMLRPCServer

HOST_PORT = ("localhost", 6789)


def double_func(num: int) -> int:
    return num * 2


server = SimpleXMLRPCServer(HOST_PORT)
server.register_function(double_func, "double_func")
server.serve_forever()
