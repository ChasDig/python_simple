from jsonrpcserver import method, serve


@method
def double_func(num: int) -> int:
    return num * 2


if __name__ == "__main__":
    serve()
