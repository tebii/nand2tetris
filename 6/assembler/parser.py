import sys

class Parser:
    """Parses the assembly file"""
    def __init__(self):
        self.file = open(sys.argv[1], "r")

        self.asm = []
        for line in self.file:
            # Get rid of whitespace 
            stripLine = line.strip()
            # ignore comments and empty lines
            if (stripLine[:2] == "//") or stripLine == "":
                continue
            self.asm.append(stripLine)
        self.asmCounter = 0 
        self.fileCounter = 0 
        self.currentInstruction = self.asm[self.asmCounter]


    def hasMoreLines(self): 
        # Next line is empty
        if (self.asmCounter) >= len(self.asm):
            return False
        return True

    def advance(self):
        # increment counter, and then make next instruction the current instruction
        self.asmCounter+=1
        self.currentInstruction = self.asm[self.asmCounter]

    def getCurrentInstruction(self):
        return self.currentInstruction
    
    







if __name__ == '__main__':
    p = Parser()
    print(p.getCurrentInstruction())
    p.advance()
    print(p.getCurrentInstruction())

