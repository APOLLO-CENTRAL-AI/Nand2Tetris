from Parser import Parser
from Code import Code
from os.path import exists
import re

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
    'None' : '000',
    'M':     '001',
    'D':     '010',
    'DM':    '011',
    'A':     '100',
    'AM':    '101',
    'AD':    '110',
    'ADM':   '111'
}

jump = {
    'None' : '000',
    'JGT':   '001',
    'JEQ':   '010',
    'JGE':   '011',
    'JLT':   '100',
    'JNE':   '101',
    'JLE':   '110',
    'JMP':   '111'
}

class Assembler():
    def __init__(self):
        # Composition
        self.Code = Code(comp, dest, jump)
        self.Parser = Parser()

        # Static
        self.greeting = '''
        Nand2Tetris
        Chapter: 06
        Prog: Assembler
        '''
        self.request = 'Enter an assembly file name in your current directory.'

        #Placeholders
        self.filepath = None
        self.asm = None

        # instructions
        self.symbol : str = None
        self.dest : str = None
        self.comp : str = None
        self.jump : str = None
        self.instruction_mode : bool = None
        self.binary = None
        self.outputfile = None

    def startup(self) -> None:
        print(
'''Nand2Tetris
Chapter: 06
Prog: Assembler without symbol table\n\n''', '*' * 50, '\n', sep = '')

    def getpath(self) -> str:
        print(self.request, ' \n')
        filepath = input()
        while (exists(filepath)) is False or \
            re.search('\.asm', filepath) is None:
            print(self.request, '\n')
            filepath = input()
        self.filepath = filepath
        self.outputfile = re.findall('\w+(?=.)', filepath)[0] + '.hack'

    def getasm(self) -> list:
        with open(self.filepath, mode = "r") as file:
            list = file.readlines()
        return list

    def writefile(self) -> None:
        with open(self.outputfile, 'w') as file:
            pass

    def writeoutput(self, input) -> None:
        with open(self.outputfile, 'a') as output:
            input = input + '\n'
            output.write(input)

    def MnemonicsToBinary(self):
        self.writefile()
        self.asm = self.getasm()
        for line in self.asm:
            self.binary = ''
            if re.search('//', line) is None:
                line = line.rstrip()
                line = line.replace(' ', '')
                self.Parser.line = line
                match(self.Parser.instructionType()):
                    case "A_INSTRUCTION":
                        self.symbol = self.Parser.symbol() if self.Parser.symbol() else '000000000000000'
                        self.binary = '0' + f'{int(self.symbol):015b}' # symbol table comes later
                        self.writeoutput(self.binary)
                    case "C_INSTRUCTION":
                        self.dest = self.Parser.dest()
                        self.jump = self.Parser.jump()
                        self.comp = self.Parser.comp()
                        self.binary = '111' + \
                            self.Code.comp(self.comp) + \
                            self.Code.dest(self.dest) + \
                            self.Code.jump(self.jump)
                        self.writeoutput(self.binary)
                    case "L_INSTRUCTION":
                        self.symbol = self.Parser.symbol() if self.Parser.symbol() else '000000000000000'
                        self.binary = '0' + f'{int(self.symbol):015b}'
                        self.writeoutput(self.binary)
            else:
                pass

if __name__ == '__main__':
    asm = Assembler()
    asm.startup()
    asm.getpath()
    asm.MnemonicsToBinary()
