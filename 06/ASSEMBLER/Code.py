class Code():
    def __init__(self, comp : dict, dest : dict, jump : dict):
        self.cmnemonic = comp
        self.dmenmonic = dest
        self.jmnemonic = jump

    def dest(self, mnemonic : str) -> str:
        return self.dmenmonic[mnemonic]

    def comp(self, mnemonic : str) -> str:
        return self.cmnemonic[mnemonic]

    def jump(self, mnemonic : str) -> str:
        return self.jmnemonic[mnemonic]
