def print_hello():
    print("Hello, World!")

def sum_numbers(a,b):
    s = a+b
    return s

def greet_user(name):
    print("Hello,",name)
    
def contains(a,b):
    t = False
    for char in a:
        if b == char:
            t = True
    return t
    
print_hello()
print(sum_numbers(3,5))
greet_user('Alice')
print(contains([1,2,3,4],3))