# Low Coupling

* A measure of how much your classes need each other.
* The lower the coupling, the more reusable it is.
* Software design often has low coupling as a goal.
* Low coupling makes refactorings easy.
* You can't completely eliminate coupling. But you can be intentional about it.
* Content coupling
  * When one method/function/class modifies directly the data of another class.
* Global coupling
  * When functions share global data.
* Control coupling
  * One module controls the flow of another part of the code via some kind of configuration.
* Stamp coupling
  * Data structures being forced to be in a certain way when it's not needed.
  * When a module relies on a certain structure but it's not being used.
* Data Coupling
  * When methods share data (normally via parameters).
* Import Coupling
  * You import a module to be able to use something
* Message Coupling
  * You connect pieces of your code by passing messages around.
* 
