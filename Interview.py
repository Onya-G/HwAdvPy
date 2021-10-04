class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, new_elem):
        self.items.append(new_elem)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def check_bracket_balance(brackets: str):
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    s = Stack()
    if len(brackets) % 2 != 0:
        return 'Not balanced'
    for i in brackets:
        if i in brackets_dict.keys():
            if s.peek() == brackets_dict[i]:
                s.pop()
            else:
                return 'Not balanced'
        elif i in brackets_dict.values():
            s.push(i)
        else:
            return 'This is not brackets'
    return 'Balanced'


if __name__ == '__main__':
    print(check_bracket_balance('[([])((([[[]]])))]{()}'))
