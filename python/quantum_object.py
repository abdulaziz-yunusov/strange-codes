"""
quantum_object.py
=================
WHAT IS THIS?
This script demonstrates two "cursed" Python paradigms using magic methods:

1. Infinite Superposition (`QuantumParadox`):
   An object that breaks classical logic. It evaluates as True to every 
   comparison operator (==, >, <) simultaneously, making it equal to, 
   greater than, and less than every value in existence.

2. Wavefunction Collapse (`QuantumState`):
   An object that exists in a superposition of multiple values. It acts as 
   a "wildcard" until it is observed (measured), at which point its state 
   permanently collapses into a single deterministic value.

3. Python Introspection:
   Techniques to bypass overridden magic methods and inspect the "true" 
   underlying identity and memory of a spoofed object.

HOW IT WORKS:
Python translates operators into special "magic methods" (dunder methods):
  - `a == b` becomes `a.__eq__(b)`
  - `a > b`  becomes `a.__gt__(b)`
  - `a < b`  becomes `a.__lt__(b)`
  - `print(a)` calls `a.__repr__()`

By overriding these methods on a class, we control how Python evaluates 
truth, comparisons, and representation at a fundamental level.
"""

import random


class QuantumParadox:
    """An object that continuously breaks classical boolean logic."""
    
    def __eq__(self, other):
        # Override '==' -> Claims to be equal to literally everything
        return True

    def __lt__(self, other):
        # Override '<' -> Claims to be strictly less than everything
        return True

    def __gt__(self, other):
        # Override '>' -> Claims to be strictly greater than everything
        return True

    def __ne__(self, other):
        # Override '!=' -> Denies being unequal to anything
        return False

    def __bool__(self):
        # Force evaluation in boolean contexts (e.g., if q:) to True
        return True

    def __hash__(self):
        # Allows usage as a key in dictionaries or elements in sets
        return 0

    def __repr__(self):
        return "<QuantumParadox: Superposition of All Possible States>"


class QuantumState:
    """An object that collapses into a classical state when observed."""

    def __init__(self, possibilities=("Dead Cat", "Alive Cat", 42, 3.14159)):
        self._possibilities = possibilities
        self._collapsed_state = None  # None indicates unobserved superposition

    def observe(self):
        """Measures the object, collapsing its wavefunction into one state."""
        if self._collapsed_state is None:
            self._collapsed_state = random.choice(self._possibilities)
        return self._collapsed_state

    def __eq__(self, other):
        # Triggers collapse upon comparison if not observed yet
        return self.observe() == other

    def __repr__(self):
        if self._collapsed_state is None:
            return f"<Superposition: {self._possibilities}>"
        return f"<Collapsed State: {self._collapsed_state}>"


# =====================================================================
# DEMONSTRATION & INTROSPECTION
# =====================================================================

if __name__ == "__main__":
    print("=" * 60)
    print(" 1. DEMONSTRATING THE LOGIC-BREAKING PARADOX ")
    print("=" * 60)
    
    q_paradox = QuantumParadox()
    print("Object String Representation:", q_paradox)
    print("Is equal to 42?             ", q_paradox == 42)
    print("Is greater than 1,000,000?   ", q_paradox > 1000000)
    print("Is less than -1,000,000?    ", q_paradox < -1000000)
    print("Is equal to 'Hello World'?  ", q_paradox == "Hello World")
    print("Is equal to None?           ", q_paradox == None)

    print("\n" + "=" * 60)
    print(" 2. INTROSPECTION: VIEWING THE TRUE VALUE ")
    print("=" * 60)
    print("To bypass the spoofed magic methods, we use low-level inspection:")
    
    # 1. 'is' operator checks memory addresses directly, bypassing __eq__
    print("\n[A] Identity check (q_paradox is 42):")
    print("    Result:", q_paradox is 42)  # False
    
    # 2. type() reveals actual class definition
    print("\n[B] Exact class type:")
    print("    Result:", type(q_paradox))  # <class '__main__.QuantumParadox'>
    
    # 3. id() returns unique memory address integer
    print("\n[C] Memory Address (ID):")
    print("    Result:", hex(id(q_paradox)))
    
    # 4. object.__repr__ bypasses custom __repr__ method
    print("\n[D] Original Object Representation:")
    print("    Result:", object.__repr__(q_paradox))

    print("\n" + "=" * 60)
    print(" 3. WAVEFUNCTION COLLAPSE DEMONSTRATION ")
    print("=" * 60)
    
    box = QuantumState()
    print("State BEFORE observation:", box)
    
    print("\nObserving the system (measuring value)...")
    measured_val = box.observe()
    print("State AFTER observation :", box)
    
    print("\nTesting consistency post-collapse:")
    print("Is it equal to measured value?", box == measured_val)
    print("Is it equal to 'Something Else'?", box == "Something Else")
