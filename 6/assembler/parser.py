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
            if (stripLine[:2] != "//") and stripLine != "":
                self.asm.append(stripLine)
        self.asmCounter = 0 
        self.fileCounter = 0 
        self.currentInstruction = self.asm[self.asmCounter]

    def hasMoreLines(self): 
        # Next line is empty
        if self.asmCounter >= len(self.asm)-1:
            return False
        return True

    def advance(self):
        # increment counter, and then make next instruction the current instruction
        self.asmCounter+=1
        self.currentInstruction = self.asm[self.asmCounter]

    def getCurrentInstruction(self):
        return self.currentInstruction

    def instructionType(self):
        if self.currentInstruction[0] == '@':
            return "A_INSTRUCTION"
        elif self.currentInstruction[0] == '(' and self.currentInstruction[-1] == ")":
            return "L_INSTRUCTION"
        else: 
            return "C_INSTRUCTION"

    def symbol(self):
        # Check if the current instruction has a symbol
        symbol = "" 
        if self.instructionType() == "A_INSTRUCTION":
            if not self.currentInstruction[1::].isnumeric():
                symbol = self.currentInstruction[1:]
        elif self.instructionType() == "L_INSTRUCTION":
            if not self.currentInstruction[1:-1].isnumeric():
                symbol = self.currentInstruction[1:-1]
        return symbol

    def dest(self):
        dest = ""
        if self.instructionType() == "C_INSTRUCTION" and "=" in self.currentInstruction:
            dest =  self.currentInstruction.split("=", 1)[0]
        elif self.instructionType() == "C_instruction" and ";" in self.currentInstruction:
            dest = self.currentInstruction.splt(";", 1)[0]
        return dest

    def comp(self):
        comp = ""
        if self.instructionType() == "C_INSTRUCTION" and "=" in self.currentInstruction:
            comp = self.currentInstruction.split("=", 1)[1]
            if ';' in comp:
                comp = comp.split(";", 0)[0]
        return comp

    def jump(self):
        jump = ""
        if self.instructionType() == "C_INSTRUCTION" and ';' in self.currentInstruction :
            jump = self.currentInstruction.split(";", 1)[1]
        return jump

if __name__ == '__main__':
    p = Parser()
    while p.hasMoreLines():
        print(p.currentInstruction)
        if p.instructionType() == "C_INSTRUCTION":
            print("dest: " + p.dest())
            print("comp: " + p.comp())
            print("jump: " + p.jump())
        p.advance()
    print(p.currentInstruction)
    if p.instructionType() == "C_INSTRUCTION":
        print("dest: " + p.dest())
        print("comp: " + p.comp())
        print("jump: " + p.jump())
