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
                print("is a comment")
                continue
            self.asm.append(stripLine)
        self.asmCounter = 0 
        self.fileCounter = 0 


    def hasMoreLines(self): 
        # Next line is empty
        if not self.file.readline():
            return False
        return True

    def getFile(self):
        return self.file
    
    







if __name__ == '__main__':
    p = Parser()
    print(p.asm)

