l = []
while True:
    c = int(input('''
    1. Push Elements
    2. Pop Elements
    3. Peek Element
    4. Display Stack
    5. Exit 
    '''))
    
    if c == 1:
        n = input("Enter the Value: ")
        l.append(n)
        print("Stack after push:", l)
        
    elif c == 2:
        if len(l) == 0:
            print("Empty Stack")
        else:
            p = l.pop()
            print(f"Popped value: {p}")
            print("Stack after pop:", l)
    
    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print("Last Stack Value:", l[-1])
    
    elif c == 4:
        print("Display Stack:", l)
    
    elif c == 5:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")
