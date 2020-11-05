# OOP example

**Step 1**
- Create an animal class

**Step 2**
- Create a reptile class, inheriting from the animal class

**Step 3**
- Create a snake class that inherits from the reptile class
- At this point, it is multi-level inheritance since the animal is the "grandparent" class for the snake class

**Step 4**
- Create a class that inherits from the snake class


**Example**
```python
    from snake import Snake

    class Python(Snake):
        def __init__(self):
            super().__init__()
            self.size = "Large"
            self.two_lungs = True
            self.venom = False


        def digest_large_prey(self):
            return "Digest prey"


        def constrict(self):
            return "Constricts prey"


        def climb(self):
            return "Does its best to climb"


        def shed_skin(self):
            return "Sheds its skin"
```

```python
# This is multi-level inheritance -- the Python class has inherited Snake while
# Snake has inherited Reptile which has inherited Animal

# We can access methods and attributes all the way up to the Animal class
# We can also change methods from Parent classes on child classes
# This does not change the methods in the Parent class

# Methods and attributes from Python class
print("From Python:")
print(python.shed_skin())
print(python.size)

# From Snake class
print("\nFrom Snake:")
print(python.limbs)
print(python.use_tongue_to_smell())


# From Reptile class
print("\nFrom Reptile:")
print(python.use_venom())
print(python.tetrapod)

# From Animal class
print("\nFrom Animal:")
print(python.alive)
print(python.procreate())

# We changed the Animal method 'eat' to something differet:
print(python.eat())
```