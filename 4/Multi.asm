@R2 // Sets R2 to 0 in case if there is any value
M=0
@R1
D=M
@i
M=D // i = RAM[1]
(LOOP)
@i // if i=. go to CONT
D=M
@END
D;JEQ
@R0
D=M
@R2 // ADD R0 to R2
M=D+M
@i
M=M-1 // i = i-1
@LOOP
0;JMP
(END)
@END
0;JMP
