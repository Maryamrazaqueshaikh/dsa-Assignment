S = []
top = None

def isEmpty(stk):
    if(stk == []):
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk) - 1

def pop(stk):
    if(isEmpty(stk)):
        return 'UnderFlow!'  
    else:
        i = stk.pop()
        if(len(stk) == 0):
            top = None
        else:
            top = len(stk) - 1
        return i

def peek(stk):
    if(isEmpty(stk)):
        return 'UnderFlow!' 
    
    else:
        top = len(stk) - 1
        return stk[top]

def display(stk):
    if(isEmpty(stk)):
        print('Stack is empty!')
    else:
        top = len(stk) - 1
        print(stk[top], '----> top')
        for i in range(top - 1, -1, -1):
            print(stk[i])

while True:
    print('STACK IMPLEMENTATION')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')

    ch = int(input('Enter the choices(1-5): '))
    
    if(ch == 1):
        item = int(input('Enter the item you want to push: '))
        push(S, item)
        print(f'{item} added successfully')
        input('Press any key to continue.....')

    elif(ch == 2):
        item = pop(S)
        if(item == 'UnderFlow!'):
            print('Stack is Empty!')
        else:
            print(f'{item} is popped')
        input('Press any key to continue...')

    elif(ch == 3):
        item = peek(S)
        if(item == 'UnderFlow!'):
            print('Stack is Empty!')
        else:
            print(f'{item} is at the top')
        input('Press any key to continue...')

    elif(ch == 4):
        display(S)
        input('Press any key to continue....')

    elif(ch == 5):
        break

    else:
        print('Please enter a valid choice between 1-5.')
        input('Press any key to continue......')
