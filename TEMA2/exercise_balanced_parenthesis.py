from stack1 import Stack1

def balanced(exp: str) -> bool:
    """Checks if the parenthesis in exp are balanced"""
    s = Stack1()
    for c in exp:
        if c == '(':
            s.push(c)
        elif c == ')':
            if s.is_empty():
                return False
            else:
                s.pop()
        else:
            # ignore any other character
            continue

    return s.is_empty()


if __name__ == '__main__':
    print('((((((())', balanced('((((((())'))
    print('(()()()())', balanced('(()()()())'))
    print('(((())))', balanced('(((())))'))
    print('()))', balanced('()))'))
    print('(()()(()', balanced('(()()(()'))
    print('(()((())()))', balanced('(()((())()))'))
