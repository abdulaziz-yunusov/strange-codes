"""
shapeshifter.py
===============
WHAT IS THIS?
Demonstrates dynamic class hijacking in Python. An instance of `Dog`
spontaneously morphs into a `Toaster` during execution.
"""

class Dog:
    def speak(self):
        return "Woof! 🐶"

class Toaster:
    def speak(self):
        return "Ping! Your toast is ready 🍞"

# Create a Dog instance
pet = Dog()
print("Initial object type :", type(pet))
print("Behavior            :", pet.speak())

print("\n... Shapeshifting in progress ...\n")

# Hijack the class type at runtime
pet.__class__ = Toaster

print("Updated object type :", type(pet))
print("Behavior            :", pet.speak())
print("Is pet an instance of Toaster?", isinstance(pet, Toaster))  # True
