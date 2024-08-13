from parser import Parser



class Code:
    """Processes C-instructions"""
    def dest(self, dest):
        match dest:
            case "null":
                return "000"
            case "M":
                return "001"
            case "D":
                return "010"
            case "DM":
                return "011"
            case "A":
                return "100"
            case "AM":
                return "101"
            case "AD":
                return "110"
            case "ADM":
                return "111"

    def comp(self, comp):
        match comp: 
            
            case "0":
                c = "101010"
            case "1":
                c = "111111"
            case "-1":
                c = "111010"
            case "D":
                c = "001100"
            case "A" | "M":
                c = "110000"
            case "!D":
                c = "001101"
            case "!A" | "!M":
                c = "110011"
            case "-D":
                c = "001111"
            case "-A" | "-M":
                c = "110011"
            case "D+1":
                c = "011111"
            case "A+1" | "M+1":
                c = "110111"
            case "D-1":
                c = "001110"
            case "A-1" | "M-1":
                c = "110010"
            case "D+A" | "D+M":
                c = "000010"
            case "D-A" | "D-M":
                c = "010011"
            case "A-D" | "M-D":
                c = "000111"
            case "D&A" | "D&M":
                c = "000000"
            case "D|A" | "D|M":
                c = "010101"
            case _:
                c = ""

        if 'M' in comp: 
            c = '1' + c
        elif 'M' not in comp:
            c = '0' + c
        return c

    def jump(self, jump):
        match jump:
            case "null":
                return "000"
            case "JGT":
                return "001"
            case "JEQ":
                return "010"
            case "JGE":
                return "011"
            case "JLT":
                return "100"
            case "JNE":
                return "101"
            case "JLE":
                return "110"
            case "JMP":
                return "111"

if __name__ == '__main__':
    c = Code()
    print("Testing dest:")
    print(c.dest("null"))
    print(c.dest("ADM"))
    print(c.dest("D"))

    print("Testing comp:")
    print(c.comp("0"))
    print(c.comp("A"))
    print(c.comp("M"))
    print(c.comp("M-1"))

    print("Testing jump:")
    print(c.jump("null"))
    print(c.jump("JGT"))
    print(c.jump("JMP"))


    

