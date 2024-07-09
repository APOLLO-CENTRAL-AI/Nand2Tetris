class Code():
    def __init__(self, comp : dict, dest : dict, jump : dict):
        self.comp = comp
        self.dest = dest
        self.jump = jump

    def dest(self, mnemonic : str) -> str:
        match(mnemonic):
            case 'M':
                return '001'
            case 'D':
                return '010'
            case 'DM':
                return '011'
            case 'A':
                return '100'
            case 'AM':
                return '101'
            case 'AD':
                return '110'
            case 'ADM':
                return '111'

    def comp(self, mnemonic : str) -> str:
        match(mnemonic):
            case '0':
                return '0101010'
            case '1':
                return '0111111'
            case '-1':
                return '0111010'
            case 'D':
                return ''

    def jump(self, mnemonic : str) -> str:
        match(mnemonic):
            case 'JGT':
                return '001'
            case 'JEQ':
                return '010'
            case 'JGE':
                return '011'
            case 'JLT':
                return '100'
            case 'JNE':
                return '101'
            case 'JLE':
                return '110'
            case 'JMP':
                return '111'