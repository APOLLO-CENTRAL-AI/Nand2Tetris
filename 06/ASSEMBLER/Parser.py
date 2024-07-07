class Parser():
    def __init__(self, asmFile : str):
        self.asmFile = asmFile

    def readasmFile(self):
        with open(self.asmFile, mode = "r") as asm:
            for line in asm.readlines():
                pass

    def hasMoreLines(self) -> bool:
        pass

    def advance(self):
        pass

    def instructionType(self) -> tuple:
        pass

    def symbol(self) -> str:
        pass

    def dest(self) -> str:
        pass

    def comp(self) -> str:
        pass

    def jump(self) -> str:
        pass