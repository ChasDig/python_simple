import msgpackrpc


class Double:
    def double_func(self, num: int) -> int:
        return num * 2


server = msgpackrpc.Server(Double())
server.listen(msgpackrpc.Address("localhost", 6789))
server.start()
