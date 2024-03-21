def post_fix(s):
    n=len(s)
    stack=[]
    for i in range (n):
        if s[i].isdigit():
            stack.append(s[i])
        elif s[i] == "+":
            a= stack.pop()
            b= stack.pop()
            stack.append(int(a) + int(b))
        elif s[i]== "*":
            a= stack.pop()
            b= stack.pop()
            stack.append(int(a) * int(b))
        elif s[i] == "-":
            a= stack.pop()
            b= stack.pop()
            stack.append(int(a) - int(b))
        elif s[i] == "/":
            a= stack.pop()
            b= stack.pop()
            stack.append(int(a) / int(b))
    return stack.pop()
s="246+*"
val=post_fix(s)
print(val)