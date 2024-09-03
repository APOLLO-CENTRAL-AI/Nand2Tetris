class Code_Writer():
    def __init_subclass__(self):
        pass

    def writeArithmetic(self, command : str) -> None:
        pass

    def writePushPop(self, command : str, index : int) -> None:
        pass

    def close(self) -> None:
        pass