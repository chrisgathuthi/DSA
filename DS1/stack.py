
def create_stack():
    stack=[]
    return stack

def check_status(stack):
    if len(stack) == 0:
        return True

def add_elem(stack,item):
    stack.append(item)
    print("the item addes is "+str(item))

def remove_elem(stack):
    return stack.pop() if check_status(stack) else stack.pop()


stack = create_stack()
add_elem(stack,12)
add_elem(stack,14)
add_elem(stack,16)
add_elem(stack,16)
add_elem(stack,16)
remove_elem(stack)
print(stack)