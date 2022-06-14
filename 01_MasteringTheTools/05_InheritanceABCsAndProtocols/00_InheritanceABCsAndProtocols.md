# Inheritance, ABCs and Protocols

* Protocols more closely resemble how Python works internally (starting with Python 3.8).
  * This relies on Python's duck typing method. 
* In the event of errors:
  * Protocols: Notice the issue when you try to use the instance.
  * ABCs: Notice the typing issue when you type to create an instance.
* ABCs belong more to a hierarchy.
* Protocols belong more closely to the place where they are used.
* With Protocols, you lose the convenience to having methods defined in super class.
* ABCs might also be useful if you have complete control over the codebase.
