# Estarta Python Training
- Instructor: Ayham Samara
- Duration: 2 Weeks
- Level: Beginner to Intermediate

## Day 1: Introduction to Python

### Interpreted vs Compiled Languages
- Interpreted languages are executed line by line, while compiled languages are transformed into machine code before execution.
- Interpreted languages offer more flexibility and ease of debugging compared to compiled languages.
- Compiled languages generally provide better performance due to optimization during the compilation process.
- the interpreter has to be present at runtime to execute the code, whereas compiled code can run independently of the compiler.
- interpreted lanaguages run the text code directly using an interpreter, while compiled languages convert the text code into machine code before execution. 
- Python is an interpreted language, which allows for easier debugging and flexibility.
- Examples of interpreted languages: Python, JavaScript, Ruby.
- Examples of compiled languages: C, C++, Rust, Go.

### Types of errors in Python 
- Syntax Errors: Occur when the code violates Python's syntax rules. Example: missing a colon or parentheses.
- Runtime Errors: Occur during program execution, often due to invalid operations. Example: division by zero.
- Import Errors: Occur when a module or package cannot be found or imported. Example: misspelling a module name.
- Logical Errors: Occur when the code runs without crashing but produces incorrect results. Example: using the wrong formula in a calculation.
- Indentation Errors: Occur when the code is not properly indented, which is crucial in Python for defining code blocks.
- Type Errors: Occur when an operation is performed on incompatible data types. Example: adding a string to an integer.
- Name Errors: Occur when a variable or function is referenced before it has been defined. Example: using a variable that hasn't been assigned a value yet.

### Virtual Environments in Python
- A virtual environment is an isolated Python environment that allows you to manage dependencies for different projects separately.
- It helps avoid conflicts between packages required by different projects.
- You can create a virtual environment using the `venv` module:
  ```bash
  python -m venv myenv
  ```
- To activate the virtual environment:
  - On Windows:
    ```bash
    myenv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source myenv/bin/activate
    ```
- To deactivate the virtual environment, simply run:
  ```bash
  deactivate
  ```
- You can install packages within the virtual environment using `pip`, and they will be isolated from the global Python installation.
- Example of installing a package:
  ```bash
  pip install requests
  ```
- To list installed packages in the virtual environment, use:
  ```bash
  pip list
  ```
- To remove a virtual environment, simply delete its directory.

### Comments in Python
- Comments are used to explain code and make it more readable.
- Single-line comments start with the `#` symbol:
  ```python
  # This is a single-line comment
  print("Hello, World!")
  ```
- Multi-line comments can be created using triple quotes (`'''` or `"""`):
  ```python
  """
  This is a multi-line comment.
  It can span multiple lines.
  """
  print("Hello, World!")
  ```
- Comments are ignored by the Python interpreter and do not affect the execution of the code.

### Python Variables
- Variables are used to store data values in Python.
- You can create a variable by assigning a value to it using the `=` operator:
  ```python
  x = 10
  name = "Alice"
  ```
- Variable names must start with a letter or an underscore and can contain letters, numbers, and underscores.
- Variable names are case-sensitive (e.g., `myVar` and `myvar` are different).
- You can assign multiple variables in a single line:
  ```python
  a, b, c = 1, 2, 3
  ```
- You can also assign the same value to multiple variables:
  ```python
  x = y = z = 0
  ```     

## Day 2: Python Basics

### package management in Python
- Python uses `pip` as its package manager to install and manage libraries and packages.
- To install a package, use the command:
  ```bash
  pip install package_name
  ```
- To install a specific version of a package, use:
  ```bash
  pip install package_name==version_number
  ```
- To upgrade a package to the latest version, use:
  ```bash
  pip install --upgrade package_name
  ```
- To uninstall a package, use:
  ```bash
  pip uninstall package_name
  ```
- To list all installed packages, use:
  ```bash
  pip list
  ```
- To search for a package, use:
  ```bash
  pip search package_name
  ```
- You can create a `requirements.txt` file to specify the packages needed for your project.
- To install packages from a `requirements.txt` file, use:
  ```bash
  pip install -r requirements.txt
  ``` 
- To freeze the current environment's packages into a `requirements.txt` file, use:
  ```bash
  pip freeze > requirements.txt
  ```

### Python Basic I/O
- Input: You can take input from the user using the `input()` function.
  ```python
  name = input("Enter your name: ")
  print("Hello, " + name)
  ```
- Output: You can display output using the `print()` function.
  ```python
  print("Hello, World!")
  ```
- You can format output using f-strings (Python 3.6+):
  ```python
  age = 25
  print(f"My name is {name} and I am {age} years old.")
  ```
- You can also use the `format()` method for formatting:
  ```python
  print("My name is {} and I am {} years old.".format(name, age))
  ```
- To print multiple items, separate them with commas:
  ```python
  print("Name:", name, "Age:", age)
  ```
- You can control the end character of the print function using the `end` parameter:
  ```python
  print("Hello,", end=" ")
  print("World!")
  ```
- You can read from and write to files using the `open()` function:
  ```python
  # Writing to a file
  with open("output.txt", "w") as file:
      file.write("Hello, World!")

  # Reading from a file
  with open("output.txt", "r") as file:
      content = file.read()
      print(content)
  ```

### Python Datatypes
- Python has several built-in data types, including:
  - Numeric Types: int, float, complex
  - Boolean Type: bool
  - String Type: str
    - In python it doesn't matter if it's a single quote or double quote
    - You can use triple quotes for multi-line strings
    - Strings are immutable, meaning you cannot change them after creation
    - Common string methods:
      - lower(): converts the string to lowercase
      - upper(): converts the string to uppercase
      - strip(): removes leading and trailing whitespace
      - split(separator): splits the string into a list based on the separator
      - join(iterable): joins elements of an iterable into a single string with the string as the separator
      - replace(old, new): replaces occurrences of a substring with a new substring
    - f-strings: formatted string literals for embedding expressions inside string literals
      - Example:
      ```python
      name = "John"
      age = 30
      greeting = f"My name is {name} and I am {age} years old."
      ```
    - format() method: another way to format strings
      - Example:
      ```python
      greeting = "My name is {} and I am {} years old.".format(name, age)
      ```
  - Sequence Types: list, tuple, range
  - List Type: list
    - Lists are ordered, mutable (can be changed), and allow duplicate elements.
    - Common list methods:
      - append(number): adds an element to the end of the list
      - insert(index, number): inserts an element at a specified index
      - remove(number): removes the first occurrence of an element from the list
      - pop(index): removes and returns the element at the specified index if no index is provided, it removes and returns the last element
      - index(value): returns the index of the first occurrence of a value in the list
      - count(value): returns the number of occurrences of a value in the list
      - sort(): sorts the list in ascending order in place
      - reverse(): reverses the order of the list
      - extend(iterable): extends the list by appending elements from an iterable
    - Examples:
      ```python
      my_list = [1, 2, 3]
      my_list.append(4)        # Adding an element
      my_list.remove(2)       # Removing an element
      print(my_list[0])       # Accessing elements  
      ```
  - Tuple Type: tuple
    - Tuples are ordered, immutable (cannot be changed), and allow duplicate elements.
    - doesn't support item assignment
    - Common tuple methods:
      - count(value): returns the number of occurrences of a value in the tuple
      - index(value): returns the index of the first occurrence of a value in the tuple
    - Examples:
      ```python
      my_tuple = (1, 2, 3)
      print(my_tuple[0])  # Accessing elements
      print(my_tuple.count(2))  # Counting occurrences
      ```
  - Set Types: set, frozenset
    - Sets are unordered, mutable (can be changed), and do not allow duplicate elements.
    - Frozensets are immutable versions of sets.
    - Common set methods:
      - add(element): adds an element to the set
      - remove(element): removes an element from the set (raises an error if not found)
      - discard(element): removes an element from the set (does not raise an error if not found)
      - union(other_set): returns a new set with elements from both sets
      - intersection(other_set): returns a new set with elements common to both sets
      - difference(other_set): returns a new set with elements in the set that are not in the other set
      - symmetric_difference(other_set): returns a new set with elements in either set but not in
    - Examples:
      ```python
      # set
      my_set = {1, 2, 3}
      my_set.add(4)          # Add element
      my_set.remove(2)       # Remove element
      another_set = {3, 4, 5}
      union_set = my_set.union(another_set)  # Union of sets
      # forzenset
      my_frozenset = frozenset([1, 2, 3])
      ```
  - Mapping Type: dict
    - Dictionaries are unordered, mutable (can be changed), and store key-value pairs.
    - Common dictionary methods:
      - keys(): returns a view of the dictionary's keys
      - values(): returns a view of the dictionary's values
      - items(): returns a view of the dictionary's key-value pairs
      - get(key): returns the value for the specified key (returns None if key not found)
      - update(other_dict): updates the dictionary with key-value pairs from another dictionary
      - pop(key): removes and returns the value for the specified key
    - Examples:
      ```python
      my_dict = {"name": "Alice", "age": 25}
      print(my_dict["name"])  # Output: Alice
      my_dict["age"] = 26     # Update age
      my_dict["city"] = "New York"  # Add new key-value pair
      ```

  - Binary Types: bytes, bytearray, memoryview
    - Bytes: Immutable sequences of bytes.
    - Bytearray: Mutable sequences of bytes.
    - Memoryview: A view object that exposes the buffer interface of an underlying binary data.
    - Examples:
      ```python
      byte_data = b"Hello"               # bytes
      byte_array = bytearray(b"Hello")   # bytearray
      mem_view = memoryview(byte_data)   # memoryview
      ```
  - Complex Types: complex
    - Complex numbers consist of a real part and an imaginary part.
    - Example:
      ```python
      complex_num = 2 + 3j
      print(complex_num.real)      # Output: 2.0
      print(complex_num.imag)      # Output: 3.0
      ```
- Python is dynamically typed, meaning you don't need to declare variable types explicitly.
- You can check the type of a variable using the `type()` function.
- Example:
  ```python
  x = 10          # int
  y = 3.14       # float
  name = "Ahmed" # str
  is_active = True # bool
  my_list = [1, 2, 3] # list
  my_complex = 2 + 3j # complex
  my_dict = {"key": "value"} # dict
  bin_data = b"Hello" # bytes
  my_set = {1, 2, 3} # set
  my_tuple = (1, 2, 3) # tuple
  print(type(x))        # Output: <class 'int'>
  ```
- You can convert between data types using type casting functions like `int()`, `float()`, `str()`, etc.
- Example:
  ```python
  num_str = "100"
  num_int = int(num_str)  # Converts string to integer
  ```
- NoneType: Python has a special data type called `NoneType`, represented by the `None` keyword, which indicates the absence of a value.

### Comparison Operators in Python
- Comparison operators are used to compare two values and return a boolean result (True or False).
- Common comparison operators in Python include:
  - Equal to (`==`): Returns True if the values are equal.
    ```python
    x == y
    ```
  - Not equal to (`!=`): Returns True if the values are not equal.
    ```python
    x != y
    ```
  - Greater than (`>`): Returns True if the left value is greater than the right value.
    ```python
    x > y
    ```
  - Less than (`<`): Returns True if the left value is less than the right value.
    ```python
    x < y
    ```
  - Greater than or equal to (`>=`): Returns True if the left value is greater than or equal to the right value.
    ```python
    x >= y
    ```
  - Less than or equal to (`<=`): Returns True if the left value is less than or equal to the right value.
    ```python
    x <= y
    ```
  - ```is```: Returns True if both variables point to the same object in memory.
    ```python
    x is y
    ```

### Boolean Operators in Python
- Boolean operators are used to combine multiple boolean expressions and return a boolean result (True or False).
- Common boolean operators in Python include:
  - `and`: Returns True if both expressions are True.
    ```python
    expr1 and expr2
    ```
  - `or`: Returns True if at least one of the expressions is True.
    ```python
    expr1 or expr2
    ```
  - `not`: Returns True if the expression is False, and False if the expression is True.
    ```python
    not expr
    ```

### Control Flow in Python
- Control flow statements allow you to control the execution of code based on certain conditions.
- Conditional Statements:
  - `if` statement: Executes a block of code if a condition is true.
    ```python
    if condition:
        # code to execute if condition is true
    ```
  - `elif` statement: Checks another condition if the previous `if` condition was false.
    ```python
    if condition1:
        # code to execute if condition1 is true
    elif condition2:
        # code to execute if condition2 is true
    ```
  - `else` statement: Executes a block of code if all previous conditions were false.
    ```python
    if condition1:
        # code to execute if condition1 is true
    else:
        # code to execute if condition1 is false
    ```
- Looping Statements:
  - `for` loop: Iterates over a sequence (like a list, tuple, or string).
    - can be used with range() to loop a specific number of times
      - Example: 
      ```python
      for i in range(5):
          print(i)
      ```
    - can also loop through characters in a string
      - Example:
      ```python
      for char in "Hello":
          print(char)
      ```
    - can also be used to loop over elements in a sequences directly
      - Example:
      ```python
      for item in sequence:
          # code to execute for each item
      ```
    - else block can be used with for loop, it will be executed when the loop is not terminated by a break statement
      - Example:
      ```python
      for item in sequence:
          # code to execute for each item
      else:
          # code to execute if loop completes without break
      ```

  - `while` loop: Repeats a block of code as long as a condition is true.
    ```python
    while condition:
        # code to execute while condition is true
    ```
- Control Flow Modifiers:
  - `break`: Exits the nearest enclosing loop.
    ```python
    for item in sequence:
        if condition:
            break  # exits the loop
    ```
  - `continue`: Skips the current iteration and moves to the next iteration of the loop.
    ```python
    for item in sequence:
        if condition:
            continue  # skips to the next iteration
    ```
  - `pass`: A placeholder that does nothing; used when a statement is syntactically required but no action is needed.
    ```python
    if condition:
        pass  # do nothing
    ```

### Functions in Python
- Functions are reusable blocks of code that perform a specific task.
- You can define a function using the `def` keyword:
  ```python
  def function_name(parameters):
      # code to execute
      return result  # optional
  ```
- You can call a function by using its name followed by parentheses:
  ```python
  function_name(arguments)
  ```
- Functions can take parameters (inputs) and return values (outputs).
- Example of a simple function:
  ```python
  def add(a, b):
      return a + b
  result = add(3, 5)
  print(result)  # Output: 8
  ```
- Functions can have default parameter values:
  ```python
  def greet(name="Guest"):
      print(f"Hello, {name}!")
  greet()          # Output: Hello, Guest!
  greet("Alice")  # Output: Hello, Alice!
  ```
- Functions can accept a variable number of arguments using `*args` and `**kwargs`:
  ```python
  def func(*args, **kwargs):
      for arg in args:
          print(arg)
      for key, value in kwargs.items():
          print(f"{key}: {value}")
  func(1, 2, 3, name="Alice", age=25)
  ```
- Functions can be nested inside other functions:
  ```python
  def outer_function():
      def inner_function():
          print("Hello from inner function!")
      inner_function()
  outer_function()
  ```
- Functions are first-class citizens in Python, meaning they can be passed as arguments to other functions, returned from functions, and assigned to variables.
- Example:
  ```python
  def square(x):
      return x * x

  def apply_function(func, value):
      return func(value)

  result = apply_function(square, 5)
  print(result)  # Output: 25
  ```
- Lambda Functions:
  - Lambda functions are small anonymous functions defined using the `lambda` keyword.
  - They can take any number of arguments but can only have a single expression.
  - Example:
    ```python
    add = lambda x, y: x + y
    result = add(3, 5)
    print(result)  # Output: 8
    ```

### Python built in functions 
-- Python provides several built-in functions that are always available for use. Some commonly used built-in functions include:
- `print(data)`: Outputs data to the console.
- `input("optional message string that will be printed on screen")`: Takes input from the user.
- `len(object)`: Returns the length of an object (e.g., string, list).
- `type(object)`: Returns the type of an object.
- `int(object)`, `float(object)`, `str(object)`: Type conversion functions.
- `range(begin, end, increment)`: Generates a sequence of numbers.
- `sum(num1, num2, ... or List)`: Returns the sum of a sequence of numbers.
- `max(num1, num2, ... or List)`, `min(num1, num2, ... or List)`: Returns the maximum or minimum value from a sequence.
- `abs(number)`: Returns the absolute value of a number.
- `round(floating point number)`: Rounds a floating-point number to the nearest integer.
- `sorted(list)`: Returns a sorted list from the elements of any iterable.
- `help()`: Provides help documentation for modules, functions, and classes.
- `dir()`: Returns a list of attributes and methods of an object.
- `enumerate(list)`: Adds a counter to an iterable and returns it as an enumerate object
- `zip()`: Combines multiple iterables into a single iterable of tuples.
- `map()`: Applies a function to all items in an iterable.
- `reduce()`: Applies a rolling computation to sequential pairs of values in an iterable.
- `filter()`: Filters items in an iterable based on a function that returns True or False.
- `eval()`: Evaluates a string as a Python expression.
- `isinstance(object, classinfo)`: Checks if an object is an instance of a specified class or a tuple of classes.


### Exception Handling in Python
- Exception handling is used to manage errors and exceptions that occur during program execution.
- You can handle exceptions using the `try`, `except`, `else`, and `finally` blocks.
- The `try` block contains code that may raise an exception.
- The `except` block contains code that runs if an exception occurs in the `try` block.
- The `else` block contains code that runs if no exceptions occur in the `try` block.
- The `finally` block contains code that runs regardless of whether an exception occurred or not.
- Example of exception handling:
  ```python
  try:
      num1 = int(input("Enter a number: "))
      num2 = int(input("Enter another number: "))
      result = num1 / num2
  except ValueError:
      print("Invalid input! Please enter numeric values.")
  except ZeroDivisionError:
      print("Error! Division by zero is not allowed.")
  except Exception as e:
      # catch-all for any other exceptions
      print(f"An unexpected error occurred: {e}")
  else:
      print(f"The result is: {result}")
  finally:
      print("Execution completed.")
  ```

## Day 3: Advanced Python Concepts

### Programming Paradigms in Python
- Python supports multiple programming paradigms, including:
  - Procedural Programming: Focuses on writing procedures or routines to perform tasks. It uses functions and control flow statements to structure code.
  - Object-Oriented Programming (OOP): Organizes code into objects that encapsulate data and behavior. It uses classes, inheritance, polymorphism, and encapsulation.
  - Functional Programming: Emphasizes the use of pure functions, higher-order functions, and immutability. It avoids changing state and mutable data.
  - Imperative Programming: Focuses on describing how a program operates through statements that change a program's state.
  - Declarative Programming: Focuses on what the program should accomplish without specifying how to achieve it. Examples include SQL and HTML.
- Python's flexibility allows developers to choose the most suitable paradigm for their specific use case or combine multiple paradigms in a single project.

### Object-Oriented Programming (OOP) in Python
- OOP is a programming paradigm that uses "objects" to represent data and behavior.
- Key concepts of OOP include:
  - Classes: Blueprints for creating objects. They define attributes (data) and methods (functions) that operate on the data.
  - Objects: Instances of classes that encapsulate data and behavior.
  - The four pillars of OOP are:
    - Encapsulation: Restricting access to certain components of an object to prevent unintended interference and misuse.
      - Example: Using private attributes and methods in a class.
    - Abstraction: Hiding complex implementation details and showing only the necessary features of an object.
      - Example: Making coffee using a coffee machine without knowing the internal workings.
    - Inheritance: Creating new classes based on existing classes to promote code reuse and establish a hierarchical relationship.
      - Example: A `Car` class inheriting from a `Vehicle` class.
    - Polymorphism: Allowing objects of different classes to be treated as objects of a common superclass, enabling flexibility and the ability to extend code.
      - Example: A function that can accept different types of objects and call their methods without knowing their specific types.

### Classes and Objects in Python
- A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that operate on the data.
- You can define a class using the `class` keyword:
  ```python
  class ClassName:
      # class attributes and methods
  ```
- An object is an instance of a class that encapsulates data and behavior.
- You can create an object by calling the class as if it were a function:
  ```python
  object_name = ClassName()
  ```
- it can have methods and attributes
- Example of a simple class and object:
  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def bark(self):
          print("Woof!")
  my_dog = Dog("Buddy", 3)
  my_dog.bark()  # Output: Woof!
  print(my_dog.name)  # Output: Buddy
  print(my_dog.age)   # Output: 3
  ```
- The `__init__` method is a special method called a constructor that initializes the object's attributes when the object is created.
- You can define methods within a class to perform actions on the object's data.
- You can access an object's attributes and methods using the dot (`.`) notation.
- Example of using methods and attributes:
  ```python
  class Circle:
      def __init__(self, radius):
          self.radius = radius
      def area(self):
          return 3.14 * self.radius ** 2
  my_circle = Circle(5)
  print(my_circle.area())  # Output: 78.5
  ```
- You can create multiple objects from the same class, each with its own set of attributes.
- Example:
  ```python
  dog1 = Dog("Max", 2)
  dog2 = Dog("Bella", 4)
  print(dog1.name)  # Output: Max
  print(dog2.name)  # Output: Bella
  ```

### Inheritance in Python
- Inheritance is a mechanism that allows a new class (child class) to inherit attributes and methods from an existing class (parent class).
- It promotes code reuse and establishes a hierarchical relationship between classes.
- You can define a child class by specifying the parent class in parentheses after the child class name:
  ```python
  class ChildClass(ParentClass):
      # child class attributes and methods
  ```
- Example of inheritance:
  ```python
  class Animal:
      def speak(self):
          print("Animal speaks")
  class Dog(Animal):
      def bark(self):
          print("Woof!")
  my_dog = Dog()
  my_dog.speak()  # Output: Animal speaks
  my_dog.bark()   # Output: Woof!
  ```
- The child class can override methods from the parent class to provide specific implementations.
- Example of method overriding:
  ```python
  class Cat(Animal):
      def speak(self):
          print("Meow!")
  my_cat = Cat()
  my_cat.speak()  # Output: Meow!
  ```
- You can use the `super()` function to call methods from the parent class within the child class.
- Example of using `super()`:
  ```python
  class Bird(Animal):
      def speak(self):
          super().speak()  # Call parent class method
          print("Chirp!")
  my_bird = Bird()
  my_bird.speak()  # Output: Animal speaks
                   #         Chirp!
  ``` 
  - Python supports multiple inheritance, allowing a child class to inherit from multiple parent classes.
  ```python
  class Parent1:
      def method1(self):
          print("Method from Parent1")
  class Parent2:
      def method2(self):
          print("Method from Parent2")
  class Child(Parent1, Parent2):
      pass
  my_child = Child()
  my_child.method1()  # Output: Method from Parent1
  my_child.method2()  # Output: Method from Parent2
  ```
### Polymorphism in Python
- Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface.
- It allows methods to be used on different objects, even if they are of different types.
- Example of polymorphism using method overriding:
  ```python
  class Dog:
      def speak(self):
          print("Woof!")
  class Cat:
      def speak(self):
          print("Meow!")
  def animal_sound(animal):
      animal.speak()
  my_dog = Dog()
  my_cat = Cat()
  animal_sound(my_dog)  # Output: Woof!
  animal_sound(my_cat)  # Output: Meow!
  ```
- Polymorphism can also be achieved through duck typing, where the type of an object is determined by the methods it defines rather than its actual class.
- Example of duck typing:
  ```python
  class Bird:
      def fly(self):
          print("Flying!")
  class Airplane:
      def fly(self):
          print("Taking off!")
  def make_it_fly(flyable):
      flyable.fly()
  my_bird = Bird()
  my_plane = Airplane()
  make_it_fly(my_bird)   # Output: Flying!
  make_it_fly(my_plane)  # Output: Taking off!
  ```

## Day 4: Common Libraries in Python


