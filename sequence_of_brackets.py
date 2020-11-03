from  ds_stack import *




def Isbalanced(str):
    stack = Stack()
    for char in str:
        if char != '(' and char != ')' and char != '[' and char != ']' and char != '{' and char != '}':
            continue
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
            continue
        if stack.empty():
            return False
        top = stack.pop()
        if top == '(' and char != ')' or top == '[' and char != ']' or top == '{' and char != '}':
            return False
    return stack.empty()

if __name__ == '__main__':
    print(Isbalanced(input()))
