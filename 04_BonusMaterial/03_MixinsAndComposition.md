# Mixins and Composition

* Mixins are a very special use case for inheritance.
  * Mixins are specific to Python.
  * Mixins relies on being able to do multiple inheritance.
* You should never create an instance of a mixin.
* You should never call super from the mixin.
* For more details, see the Mixins lectures.
* Django uses Mixins a lot.
* Most languages don't allow multiple inheritance.
* See examples in 03_BeingAResponsibleDeveloper/01_Mixins
* In the course video we talk about the problems with mixins
  * Ex: the order matters, multiple inheritance, method overloading, limit basic functionality.
  * Mixins make code way harder to change. 
    * If you break the mixins rules, you're going to have to refactor all the things.
  * Typing support can't handle mixins quite well.
  * You can't add a dataclass without a lot of risk.
  * With mixins, it's hard to introduce inheritance due to intense coupling.
  * Testing with mixins is difficult because you are not supposed to create instances of mixins.
* What to do instead of Mixins?
  * You can just make a pure function if you don't need an instance variable.
  * If you do need instance variables, just pass it as a value.
  * Favor composition over inheritance.
    * Instead of an "is-a" relationship use a "has-a" relationship.
