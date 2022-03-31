mass = [1,2,3,10,5]

class Stack:
    def __init__(self):
        self.mass = mass

    def isEmpty (self):
        if len(mass) == 0:
            return True
        else:
            return False

    def push(self, item):
        mass.append(item)

    def pop(self):
        removed = mass.pop()
        return mass[-1]

    def peek(self):
        return mass[-1]

    def size(self):
        return len(mass)



    def stroke(self, stroka):
        listt = []
        my_list = []
        for i in stroka:
            listt.append(i)
        for y in listt:
            if y == '(' or y == '[' or y == '{':
                my_list.append(y)
            else:
                if len(my_list) > 1:
                    if my_list[-1] == '(' and y == ')':
                        my_list.pop()
                    elif my_list[-1] == '[' and y == ']':
                        my_list.pop()
                    elif my_list[-1] == '{' and y == '}':
                        my_list.pop()
                    else:
                        return 'Несбалансированно'
                elif len(my_list) == 1:
                    if my_list[0] == '(' and y == ')':
                        my_list.pop()
                    elif my_list[0] == '[' and y == ']':
                        my_list.pop()
                    elif my_list[0] == '{' and y == '}':
                        my_list.pop()
                    else:
                        return 'Несбалансированно'
                else:
                    return 'Несбалансированно'
        if len(my_list) == 0:
            return 'Сбалансированно'


print(Stack().isEmpty())
print(Stack().pop())
print(Stack().peek())
print(Stack().size())
print(Stack().stroke('{{[()]}}'))
