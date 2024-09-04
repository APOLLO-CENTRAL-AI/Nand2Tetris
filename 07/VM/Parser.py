class Parser():
    def __init__(self, file_path : str):
        with open(file_path, 'r') as reader:
            self.line = reader.readline()
            while self.hasmorelines() is True:
               self.line = reader.readline()

    def hasmorelines(self) -> bool:
        if self.line != '':
            return True
        else:
            return False
        

    def advance(self) -> None:
        pass

    def command_type(self) -> str:
        pass

    def arg1(self) -> str:
        pass

    def arg2(self) -> int:
        pass