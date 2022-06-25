# Final Thoughts

* The only dependency for `payment` is now just the `PaymentStatus`.
* The main file is dealing with the dirty details (specific implementation details).
  * But this is the only place we do this!
  * This is a sign of a great design.
  * If you have different settings all over the place, this is a sign of a bad design.
* This also helps you very easily write tests in a specific spot.
* Bridge pattern
  * Variety 1: What we did with the PaymentProcessor
  * Variety 2: What we did for the Authorizer functions
  * The concept of the bridge pattern is more important than the specifics. 
  * The important idea is to rely on abstractions. Think more about less coupling and more cohesion.
