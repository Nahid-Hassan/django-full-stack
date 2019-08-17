"""
Python Scope:
    1. Local
    2. Enclosing Function locals
    3. Global
    4. Built-in
"""

#Enclosing function locals
value = 100

def changed_global_value():
    # global value
    value = 50

    return value;

print('Before function call ', value)
value = changed_global_value()
print('After function calling ',value)