# Introduction and Analysis

* Most design patterns rely on using an abstraction mechanism.
* In Python, we have the following abstraction mechanisms:
  * Abstract Base Classes
  * Protocols
* We can reduce coupling by introducing abstractions.
* It's about recognizing where there is coupling.
* Existing dependencies:
  * None in authorization.py
  * None in data.py
  * Order relies on PaymentStatus
  * Main relies on Order and LineItem and PaymentProcessor
