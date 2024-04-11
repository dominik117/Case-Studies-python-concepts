# Global variable
x = "global x"

def test():
    # This is a local variable, it shadows the global x
    x = "local x"
    print(x)

def test_global_keyword():
    global x
    # Now, this x refers to the global x, changes here will affect the global x
    x = "changed global x"

def test_enclosing_scope():
    # Enclosing variable
    y = "enclosing y"
    def inner():
        # The inner function can access y, the variable in the enclosing scope
        print(y)
    inner()

# Calling functions to see the effect of scopes and shadowing
print(x)  # Prints the global x
test()  # Prints the local x, demonstrating shadowing
print(x)  # Still prints the global x, showing that test() didn't affect it

test_global_keyword()  # This will change the global x
print(x)  # Now it prints the changed global x

test_enclosing_scope()  # Demonstrates accessing an enclosing scope variable
