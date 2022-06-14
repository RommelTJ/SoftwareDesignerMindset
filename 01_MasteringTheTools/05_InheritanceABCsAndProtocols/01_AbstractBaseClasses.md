# Abstract Base Classes

* Inheritance allows you to define an interface to a program without relying on a specific implementation.
* It's also dangerous. Because the relationship is very strong. Strong coupling.
* Since Python doesn't have interfaces, you can use Abstract Base Classes (ABCs).
  * An ABC is a class that defines an interface. You are not allowed to instantiate them.
  * They protect you from creating an instance that is not fully complete.
    * If you try to implement a class that doesn't implement all of its `abstractmethod` methods, 
      it will complain with a `TypeError`.
  * But type hints are ignored by the compiler.
    * Ex: You can remove the inheritance from the Car class and the code will still run, 
          but tools like PyLance will complain about missing "Expected Vehicle type".
