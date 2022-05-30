# Inheritance, ABCs and Protocols

* Inheritance allows you to define an interface to a program without relying on a specific implementation.
* It's also dangerous. Because the relationship is very strong. Strong coupling.
* Since Python doesn't have interfaces, you can use Abstract Base Classes (ABCs).
  * They protect you from creating an instance that is not fully complete.
  * But type hints are ignored by the compiler.
* Protocols more closely resemble how Python works internally (starting with Python 3.8).
  * This relies on Python's duck typing method. 
* In the event of errors:
  * Protocols: Notice the issue when you try to use the instance.
  * ABCs: Notice the typing issue when you type to create an instance.
* ABCs belong more to a hierarchy.
* Protocols belong more closely to the place where they are used.
* With Protocols, you lose the convenience to having methods defined in super class.
* ABCs might also be useful if you have complete control over the codebase.
