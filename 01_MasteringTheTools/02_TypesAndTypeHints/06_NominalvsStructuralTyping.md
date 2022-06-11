# Nominal vs Structural Typing

* Structural vs Nominal typing
    * Nominal: If you inherit from a type, you are of that type.
    * Structural: If you have the same shape as a type, you are of that type.
        * Duck typing is an example of Structural typing.
* You can call len on any object that has a __len__ method. This is a simple example of duck-typing.
    * If it has a __len__ function, you can get its length.
    * If an object adheres to this protocol, then it is of that type.
