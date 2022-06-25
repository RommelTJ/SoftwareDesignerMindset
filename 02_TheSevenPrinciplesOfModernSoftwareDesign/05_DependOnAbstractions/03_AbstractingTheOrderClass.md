# Abstracting the Order Class

* See code example.
* The PaymentProcessor is dependent on the Order class.
  * If you look at what it actually uses, it just gets the total price and sets the status
  * We generalize this with an abstraction: Something that has a total price and sets a status.
  * We do this via a Protocol.

