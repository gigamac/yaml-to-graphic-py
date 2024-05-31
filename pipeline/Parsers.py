class ParserFunction:
    pattern = ''
    function = None

    def __init__(self,pattern,function):
        self.pattern = pattern
        self.function = function
        print(self)
