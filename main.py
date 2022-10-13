class Stack(list):

    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.isEmpty():
            item = self[-1]
            self.__delitem__(-1)
        return item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def lifo(seq):
    stack = Stack()
    is_good = True
    for i in seq:
        if i in '[{(':
            stack.push(i)
        elif i in '}])':
            if not stack:
                is_good = False
                break
            open_brack = stack.pop()
            if open_brack == '(' and i == ')':
                continue
            if open_brack == '[' and i == ']':
                continue
            if open_brack == '{' and i == '}':
                continue
            is_good = False
            break
    if is_good and stack.size() == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    s = input('Введите скобочную последовательность: ')
    lifo(s)
