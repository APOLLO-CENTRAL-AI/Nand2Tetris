import re

class Parser():
    def __init__(self):
        self.line = None

    def hasMoreLines(self) -> bool:
        pass # Python's context manager makes this method redundant

    def advance(self):
        pass # Python's context manager makes this method redundant

    def instructionType(self) -> str:
        if re.search('(?<=@).+', self.line):
            return 'A_INSTRUCTION'
        elif re.search('\w+(?==|;)', self.line):
            return 'C_INSTRUCTION'
        elif re.search('(?<=\()[^)]+(?=\))', self.line):
            return "L_INSTRUCTION"
        else:
            pass

    def symbol(self) -> str:
        breakpoint()
        return re.findall('(?<=@|\()[^)]+', self.line)[0] \
        if re.search('(?<=@|\()[^)]+', self.line) else '000000000000000'

    def dest(self) -> str:
        breakpoint()
        return re.findall("\w+(?==)", self.line)[0] \
        if re.search("\w+(?==)", self.line) else '000'

    def comp(self) -> str:
        breakpoint()
        return re.findall('(?<==).+', self.line)[0] \
        if re.search('=', self.line) else re.findall('\w+(?=;)', self.line)[0]

    def jump(self) -> str:
        breakpoint()
        return re.findall("(?<=;)\w+", self.line)[0] \
        if re.search("(?<=;)\w+", self.line) else '000'