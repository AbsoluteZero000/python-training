# Estarta Python Training

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


### Python Datatypes
- Python has several built-in data types, including:
  - Numeric Types: int, float, complex
  - Sequence Types: list, tuple, range
  - Text Type: str
  - Set Types: set, frozenset
  - Mapping Type: dict
  - Boolean Type: bool
  - Binary Types: bytes, bytearray, memoryview
- Python is dynamically typed, meaning you don't need to declare variable types explicitly.
- You can check the type of a variable using the `type()` function.
- Example:
  ```python
  x = 10          # int
  y = 3.14       # float
  name = "Alice" # str
  is_active = True # bool
  ```


### Types of errors in Python 
- Syntax Errors: Occur when the code violates Python's syntax rules. Example: missing a colon or parentheses.
- Runtime Errors: Occur during program execution, often due to invalid operations. Example: division by zero.
- Logical Errors: Occur when the code runs without crashing but produces incorrect results. Example: using the wrong formula in a calculation.
- Indentation Errors: Occur when the code is not properly indented, which is crucial in Python for defining code blocks.
- Type Errors: Occur when an operation is performed on incompatible data types. Example: adding a string to an integer.
- Name Errors: Occur when a variable or function is referenced before it has been defined. Example: using a variable that hasn't been assigned a value yet.
- Import Errors: Occur when a module or package cannot be found or imported. Example: misspelling a module name.

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
