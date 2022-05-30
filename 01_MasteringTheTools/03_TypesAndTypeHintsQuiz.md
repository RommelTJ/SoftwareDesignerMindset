# Types and Type Hints Quiz

1. What's the main reason to add type hints to your Python program?  
A: Type hints help you as a developer to understand and edit your own code better.

2. In a GUI application, we keep track of the actions that a user has taken, in order to support undo and redo behavior. 
Each action is represented by a class which is a subclass of Action, for example: EditAction, DeleteAction, 
SelectAction, ReplaceAction. There's also a function get_past_actions, that return the actions the user did in the 
past. What's the return type of this function?  
A: list[Action]

3. Consider the following function:
`def compute_average(numbers: list[float]) -> float`
which computes the average of a list of floating point numbers. Now consider this assignment:
`a = compute_average`. What's the type of a?  
A: Callable[[list[float]], float]

4. Which of the following statements is true?  
A: The int type in Python can represent an arbitrarily large number (limited only by the memory of the machine the 
code is running on).   
Regular strings and formatted strings (f-strings) have the same type: str.   
A function in Python always has the Callable type.  

5. When is typing information gathered in a dynamically typed language?    
A: At runtime.

6. How can we classify the type system that Python uses?    
A: Dynamically and strongly typed.  

7. Why does the expression "Hello" + 20 result in an error in Python?  
A: Python is strongly typed

8. In Python, you're allowed to assign values of different types to the same variable:  
`a = 4`
`a = True`
What does this say about Python's type system?  
A: Python is dynamically typed.

