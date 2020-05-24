import random
def ascii_to_chr(n):
    return chr(int(n)) if n.isdigit() else n
def interpret(code):
    print(code)
    code = code.split("\n")
    
    output = ""
    stack=[]
    row = 0
    col = 0
    mode = "num"
    direction = "E"
    count = 0
    while code[row][col]!="@":    
        char = code[row][col]
        print(char, stack, output, row, col)
        if char!= '"' and (mode=="alphanum" or char.isdigit()):
            stack.append(char)
        if char=="+":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(a)+int(b)))
        if char=="-":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(b)-int(a)))
        if char=="*":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(a)*int(b)))
        if char=="/":
            a = stack.pop()
            b = stack.pop()

            stack.append(str(int(b)//int(a)) if a!="0" else "0")
        if char=="%":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(b)%int(a)) if a!="0" else "0")
        elif char == ">":
            direction = "E"
        elif char == "<":
            direction = "W"
        elif char == "^":
            direction = "N"
        elif char == "v":
            direction = "S"
        elif char == "?":
            direction = random.choice(["N", "S", "E", "W"])
        elif char =="_":
            value = stack.pop()
            if value=="0":
                direction = "E"
            else:
                direction = "W"
        elif char =="|":
            value = stack.pop()
            if value=="0":
                direction = "S"
            else:
                direction = "N"
        elif char =='"':
            mode = "alphanum" if mode=="num" else "num"
        elif char ==".":
            output+="".join(stack[::-1])
            stack = []
        elif char ==",":
            output+= "".join(map(ascii_to_chr, stack[::-1]))
            stack = []
        elif char =="#":
            if direction == "E":
                col += 1
            elif direction == "W":
                col -= 1 
            elif direction == "N":
                row -= 1
            elif direction == "S":
                row += 1
        elif char == ":":
            if len(stack)==0:
                stack.append("0")
            else:
                stack.append(stack[-1])
        elif char =="\\":
            if len(stack)==1:
                stack.append("0")
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif char =="g":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(str(ord(code[y][x])))
        elif char =="$":
            stack.pop()
        if direction == "E":
            col += 1
        elif direction == "W":
            col -= 1 
        elif direction == "N":
            row -= 1
        elif direction == "S":
            row += 1
        count+=1

    return output
print(interpret('>987v>.v\nv456<  :\n>321 ^ _@')== '123456789')
print(interpret('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^')=='Hello World!\n')
print(interpret('08>:1-:v v *_$.@\n  ^    _$>\\:^   '))
