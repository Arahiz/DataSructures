from  ds_stack import *




def Isbalanced(str):
    stack = Stack()
    stack_index_open_brackets = Stack()
    count = 0
    for char in str:
        count += 1
        if char != '(' and char != ')' and char != '[' and char != ']' and char != '{' and char != '}':
            continue
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
            stack_index_open_brackets.push(count)
            continue
        if stack.empty():
            return count
        top = stack.pop()
        if top == '(' and char != ')' or top == '[' and char != ']' or top == '{' and char != '}':
            return count
        stack_index_open_brackets.pop()
    if not  stack.empty():
        return stack_index_open_brackets.pop()
    return "Success"

if __name__ == '__main__':
    print(Isbalanced(input()))
