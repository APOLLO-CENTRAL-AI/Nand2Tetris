from Parser import Parser
from Code import Code

class Assembler():
    def __init__(self, asmFile):
        self.Code = Code()
        self.Parser = Parser()
        self.asm = self.readasmFile(asmFile)

    def readasmFile(self, asmFile : str) -> list:
       with open(asmFile, mode = "r") as file:
            return file.readlines()

    def MnemonicsToBinary(self):
        for line in self.asm:
            self.Parser.line = line
            match(self.Parser.instructionType()):
                case "A_INSTRUCTION":
                    self.Parser.symbol()
                case "C_INSTRUCTION":
                    self.Parser.dest()
                    self.Parser.comp()
                    self.Parser.jump()
                case "L_INSTRUCTION":
                    self.Parser.symbol()
