# Abstracting the Authorizer Functions

* See code example.
* In initializer, we pass a type and assign to the correct authorizer function.
  * Thus, this file needs to know about every authorizer function.
* Payment class
  * Responsible for debit and credit payments
  * Responsible for collecting the specific authorization function
    * We solve this by giving the initializer a function reference.
    * Or in an object-oriented way, we use the Strategy Pattern.
      * Being too strict on design patterns may not be optimal since it can be verbose, and 
        functional features can accomplish the same thing.
