import zerorpc


class RPC:
    def sum_func(self, num_a, num_b):
        return num_a + num_b


server = zerorpc.Server(RPC())
server.bind("tcp://127.0.0.1:4242")
server.run()
