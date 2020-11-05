# OOP example
1. Create an animal class
2. Create a reptile class, inheriting from the animal class
3. Create a snake class that inherits from the reptile class. At this point, it is multi-level inheritance since the animal is the "grandparent" class for the snake class
4. Create a class that inherits from the snake class


**Example**
```python
    # This is the final class created
    # It's parent classes are found in the directory
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

**```__name__``` and ```__main__```**
- These are used to check if the code is run from the current file or a different file.

```python
# This is mod1.py
# If you run this file, __name__ is __main__
print("This is mod1.py, name is: ", __name__)

def check():
    print("From mod1.py")

if __name__ == "__main__":
    main()

####### OUTPUT when running 'python3 mod1.py'
# This is mod1.py, name is:  __main__
# From mod1.py
```

```python
# This is mod2.py
import mod1

####### OUTPUT when running 'python3 mod2.py'
# This is mod1.py, name is:  mod1
```

```python
# This happens because when you import a module from another file, that file is no longer called __main__

# Whenever the interpreter reads a source file, it sets the variable __name__
# and then executes all files in that file
# When you import mod1, the interpreter sets the __name__ of the import as mod1
# When it runs the mod1 file (since you've imported it), it's __name__ is no longer '__main__' hence the function check() does not run

if __name__ == "__main__":
    check()


```
---
Links:
- [1](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
