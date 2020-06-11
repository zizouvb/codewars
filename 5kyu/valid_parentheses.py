def valid_parentheses(string):
    stack=[]
    for c in string:
        if c=="(":
            stack.append(c)
        elif c==")":
            if not stack or stack.pop() !="(":
                return False
         
    return len(stack)==0
