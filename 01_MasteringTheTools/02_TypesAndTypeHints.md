# Types and Type Hints

* Python has types.
* Static vs Dynamic typing is whether the type checking happens at compile time or run time.
* Strong vs Weak typing is when certain types can be automatically converted, 
  * Ex: Converting string to number or Int to Double.
* Python is a dynamically-typed language, but it is also strongly-typed.
* You can re-assign types because it's dynamically typed. You can't do this in a static language like Java.
* But Python is also Strongly typed.
* A tool like Pylance helps you detect these sorts of mistakes.
* You can add type hints to function in python, but the compiler won't stop you. They are ignored by the interpreter.
  * These are also ignored by the interpreter.
* Python functions are Callable. Also ignored by the interpreter.
* Without types and type hints, you don't know what is being called except by reading docs or implementation.
* Use types to clarify what you want.
* Python is strongly and dynamically typed.
* Structural vs Nominal typing
  * Nominal: If you inherit from a type, you are of that type.
  * Structural: If you have the same shape as a type, you are of that type.
* You can call len on any object that has a __len__ method. This is a simple example of duck-typing.
  * If it has a __len__ function, you can get its length.
  * If an object adheres to this protocol, then it is of that type.
* Pros
  * Good for working with a team
  * Good for catching errors early
* Cons
  * Complex types may lead to cryptic error messages. Ex: Typescript with its complicated types.
  * Types may restrict functionality.
  * Types are not yet that common in Python packages.
