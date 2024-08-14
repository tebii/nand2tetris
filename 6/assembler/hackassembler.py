from code import Code
from parser import Parser
from symboltable import SymbolTable
import sys


class HackAssembler:
    def __init__(self):
        self.p = Parser(sys.argv[1])
        self.c = Code()
        self.s = SymbolTable()
        self.asmOutput = []


    def firstPass(self):
        # First pass of the file, focusing only on (label) declarations, then add them to the symbol table
        pc = 0
        while True: 
            if self.p.instructionType() == "L_INSTRUCTION":
                self.s.addEntry(self.p.symbol(), pc)
            else:
                pc+=1
            if self.p.hasMoreLines() == True:
                self.p.advance()
            else: 
                break

    def secondPass(self):
        # reset parser for second pass
        self.p = Parser(sys.argv[1])
        ramAddr = 16
        currentInstruction = ""
        a = ""
        while True:
            if self.p.instructionType() == "A_INSTRUCTION":
                # instruction type has a label
                if self.p.symbol() != "null":
                    if self.s.contains(self.p.symbol()) == False:
                        self.s.addEntry(self.p.symbol(), ramAddr)
                        a = ramAddr
                        ramAddr += 1
                    elif self.s.contains(self.p.symbol()): 
                        # found symbol in SymbolTable
                        a = self.s.getAddress(self.p.symbol())
                else:
                    a = self.p.getCurrentInstruction()[1::]
                currentInstruction = "0" + f'{int(a):015b}'

            elif self.p.instructionType() == "C_INSTRUCTION":
                currentInstruction = "111" + self.c.comp(self.p.comp()) + self.c.dest(self.p.dest()) + self.c.jump(self.p.jump())
            elif self.p.instructionType() == "L_INSTRUCTION":
                self.p.advance()
                continue
            self.asmOutput.append(currentInstruction)

            if self.p.hasMoreLines() == True:
                self.p.advance()
            else:
                break

    def writeToFile(self):
        filename = sys.argv[1].split(".", 1)[0] + ".hack"
        f = open(filename, "w")
        f.write("")
        f = open(filename, "a")
        for line in self.asmOutput:
            f.write(line + "\n")
        f.close()

     

    
if __name__ == "__main__":
    h = HackAssembler()
    h.firstPass()
    h.secondPass()
    h.writeToFile()



