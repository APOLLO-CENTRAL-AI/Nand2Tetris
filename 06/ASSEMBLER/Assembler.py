from Parser import Parser
from Code import Code

comp = {
    '0':    '0101010',
    '1':    '0111111',
    '-1':   '0111010',
    'D':    '0001100',
    'A':    '0110000',
    'M':    '1110000',
    '!D':   '0001101',
    '!A':   '0110001',
    '!M':   '1110001',
    '-D':   '0001111',
    '-A':   '0110011',
    '-M':   '1110011',
    'D+1':  '0011111',
    'A+1':  '0110111',
    'M+1':  '1110111',
    'D-1':  '0001110',
    'A-1':  '0110010',
    'M-1':  '1110010',
    'D+A':  '0000010',
    'D+M':  '1000010',
    'D-A':  '0010011',
    'D-M':  '1010011',
    'A-D':  '0000111',
    'M-D':  '1000111',
    'D&A':  '0000000',
    'D&M':  '1000000',
    'D|A':  '0010101',
    'D|M':  '1010101'
}

dest = {
    'M':     '001',
    'D':     '010',
    'DM':    '011',
    'A':     '100',
    'AM':    '101',
    'AD':    '110',
    'ADM':   '111'
}

jump = {
    'JGT':   '001',
    'JEQ':   '010',
    'JGE':   '011',
    'JLT':   '100',
    'JNE':   '101',
    'JLE':   '110',
    'JMP':   '111'
}

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
                    try:
                        dest = self.Code.dest(self.Parser.dest())
                    except:
                        dest = '000'
                    try:
                        jump = self.Code.jump(self.Parser.jump())
                    except:
                        jump = '000'
                    comp = self.Code.comp(self.Parser.comp())
                case "L_INSTRUCTION":
                    self.Parser.symbol()
