# demo.py
def greet(name):
    if not name:
        return "Hello, Stranger"
    return f"Hello, {name}"

print(greet(""))
