# Analysis Of What We've Done

* Because we thought carefully of how we set things up, now it's easy to be flexible with Payment sources.
* We generalized how things are composed.
* We have a Protocol that defines how a payment source works.
* We have a main method where there is a single spot to specify a class (the dirty place).
* Instead of splitting things out by using inheritance, we're using composition.
* You could've also used Abstract Base Classes, but Protocols are cleaner.
