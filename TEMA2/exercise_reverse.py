from stack1 import Stack1

def reverse(word: str) -> str:
    """ Returns the reverse word of the input word.
    It uses a stack"""
    s = Stack1()
    # saves each character onto the stack
    for c in word:
        s.push(c)

    # variable to save the reverse word
    reverse_word = ''
    while not s.is_empty():
        # pops from the stack
        c = s.pop()
        # appends at the end of the reverse word
        reverse_word += c

    return reverse_word


if __name__ == '__main__':
    w = 'horse'
    print('reverse word for {}: {}'.format(w, reverse(w)))
    w = 'amor'
    print('reverse word for {}: {}'.format(w, reverse(w)))
    w = 'radar'
    print('reverse word for {}: {}'.format(w, reverse(w)))
