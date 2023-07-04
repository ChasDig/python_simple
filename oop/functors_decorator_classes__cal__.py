# __call__

class StripChars:

    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError(f"Аргумент {args[0]} долже быть строкой")
        return args[0].strip(self.__chars)


strip = ":!?Hello world?:!"
strip_chars_1 = StripChars("!?:")

print(strip)
result = strip_chars_1(strip)
print(result)


# Decorator


class DecorSum:

    def __init__(self, func):
        self.__func = func

    def __call__(self, arg_1, arg_2, *args, **kwargs):
        print("Decorator!")
        return self.__func(arg_1, arg_2)


@DecorSum
def create_sum(arg_1, arg_2):
    return arg_1 + arg_2


print(create_sum(1, 2))
