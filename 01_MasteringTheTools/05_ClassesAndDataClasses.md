# Classes and Data Classes

* Printing a class instance will give you a memory address.
* A Class is a representation of objects. What behavior is available when you have an object of that type.
* Data Classes provide a basic implementation of a data-oriented class and removes boilerplate code.
  * You can make a field uninitializable by adding init=False to the field value.
  * If you don't want to use a default_factory, you can also remove the default_factory but add a post_init dunder method
  * You can add `@dataclass(frozen=True)` to prevent a class from being modified
* Encapsulation helps to separate code better. Less coupling of your code.
  * Data Classes encourages coupling because it allows you access to instance variables.
  * Python has an unwritten convention with "_" that makes a variable private.
