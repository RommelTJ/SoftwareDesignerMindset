# Types and Type Hints

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
