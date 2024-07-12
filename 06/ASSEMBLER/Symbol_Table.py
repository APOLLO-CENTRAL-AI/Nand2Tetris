class SymbolTable():
    def __init__(self):
        self.symtable = {}

    def addEntry(self, symbol : str, address : int) -> None:
        self.symtable[symbol] = address

    def contains(self, symbol : str) -> bool:
        return True if symbol in self.symtable.keys() else False

    def getAddress(self, symbol : str) -> int:
        return self.symtable[symbol]
