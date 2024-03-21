def isBalanced(exp):
    stack=[]
    for char in exp:
        if char in [ '(','{','[']:
            stack.append(char)
        else:
            if not stack:
                return False
            cur = stack.pop()
            if cur =='(' and char!=')':
                return False
            if cur =='{' and char!='}':
                return False
            if cur =='[' and char!=']':
                return False
    if stack:
        return False
    else:
        return True
expr = input("Enter an expression :") 
if isBalanced(expr):
    print("Balanced")
else:
    print("Unbalanced")