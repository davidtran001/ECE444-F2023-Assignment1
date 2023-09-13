class utils:
    def reversed(num):
        if isinstance(num, int):
            return int(str(num)[::-1])
        else:
            raise TypeError()

    def formatter(num):
        if isinstance(num, int):
            return bin(num), oct(num)
        else:
            raise TypeError()
