class Connection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def _create_connection(self) -> None:
        print(f"Connected was created! Port={self.port}, host={self.host}")

    def __del__(self):
        Connection.__instance = None


con_1 = Connection("localhost", 5432)
con_2 = Connection("127.0.0.1", 5433)

print(id(con_1), id(con_2))
print(con_1 is con_2)
