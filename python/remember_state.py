def remember_state(item, state_store=[]):
    """
    A function without global variables or class objects that maintains state 
    between function calls by abusing default argument evaluation behavior.
    """
    state_store.append(item)
    return state_store

print(remember_state("First"))   # ['First']
print(remember_state("Second"))  # ['First', 'Second']
print(remember_state("Third"))   # ['First', 'Second', 'Third']

# Inspecting the function's secret internal memory tuple:
print("\nFunction's internal __defaults__ tuple:")
print(remember_state.__defaults__)  # (['First', 'Second', 'Third'],)
