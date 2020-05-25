import random


def ascii_to_chr(n):
    return chr(int(n)) if n.isdigit() else n


def interpret(code):
    print(code)
    code = code.split("\n")

    output = ""
    stack = []
    row = 0
    col = 0
    mode = "num"
    direction = "E"
    count = 0
    while code[row][col] != "@":
        char = code[row][col]
        print(char, stack, output, row, col)
        if char != '"' and mode == "alphanum":
            stack.append(str(ord(char)))
        elif char.isdigit():
            stack.append(char)
        elif char == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(a)+int(b)))
        elif char == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(b)-int(a)))
        elif char == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(a)*int(b)))
        elif char == "/":
            a = stack.pop()
            b = stack.pop()

            stack.append(str(int(b)//int(a)) if a != "0" else "0")
        elif char == "%":
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(b) % int(a)) if a != "0" else "0")
        elif char == "!":
            stack.append("1" if int(stack.pop()) == 0 else "0")
        elif char == "`":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append("1" if b > a else "0")
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
        elif char == "_":
            value = stack.pop()
            if value == "0":
                direction = "E"
            else:
                direction = "W"
        elif char == "|":
            value = stack.pop()
            if value == "0":
                direction = "S"
            else:
                direction = "N"
        elif char == '"':
            mode = "alphanum" if mode == "num" else "num"
        elif char == ":":
            if len(stack) == 0:
                stack.append("0")
            else:
                stack.append(stack[-1])
        elif char == "\\":
            if len(stack) == 1:
                stack.append("0")
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif char == "$":
            stack.pop()
        elif char == ".":
            output += stack.pop()
        elif char == ",":
            output += ascii_to_chr(stack.pop())
        elif char == "#":
            if direction == "E":
                col += 1
            elif direction == "W":
                col -= 1
            elif direction == "N":
                row -= 1
            elif direction == "S":
                row += 1
        elif char == "g":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(str(ord(code[y][x])))
        elif char == "p":
            y = int(stack.pop())
            x = int(stack.pop())
            v = int(stack.pop())
            y_row = list(code[y])
            y_row[x]=str(v)
            code[y] = "".join(y_row)           
        if direction == "E":
            col += 1
        elif direction == "W":
            col -= 1
        elif direction == "N":
            row -= 1
        elif direction == "S":
            row += 1
        count += 1

    return output

