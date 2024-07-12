class SymbolTable():
    def __init__(self):
        self.symtable = {
            'R0' : 0,
            'R1' : 1,
            'R2' : 2,
            'R3' : 3,
            'R4' : 4,
            'R5' : 5,
            'R6' : 6,
            'R7' : 7,
            'R8' : 8,
            'R9' : 9,
            'R10' : 10,
            'R11' : 11,
            'R12' : 12,
            'R13' : 13,
            'R14' : 14,
            'R15' : 15,
            'SP' : 0,
            'LCL' : 1,
            'ARG': 2,
            'THIS' : 3,
            'THAT': 4,
            'SCREEN' : 16384,
            'KBD' : 24576
        }
        # symbol : str -> address : int

    def addEntry(self, symbol : str, address : int) -> None:
        self.symtable[symbol] = address

    def contains(self, symbol : str) -> bool:
        return True if symbol in self.symtable.keys() else False

    def getAddress(self, symbol : str) -> int:
        return self.symtable[symbol]
