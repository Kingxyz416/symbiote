def infix_to_postfix(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    stack = []
    postfix = ""

    for ch in expression:

        
        if ch.isalnum():
            postfix += ch

        
        elif ch == '(':
            stack.append(ch)

        
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # remove '('

        
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(ch, 0) <= precedence.get(stack[-1], 0)):
                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


exp = "(A+B)*C"
print(infix_to_postfix(exp))