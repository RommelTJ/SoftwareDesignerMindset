# Why you need to be careful with Mixins

* The idea of injecting extra behavior to a class seems nice but,
  * The order that you add mixins matters. In Python, it goes from right-to-left.
    * Thus, the program only works because SalariedEmployee is to the right of Commission.
    * This also applies to methods in the mixed in behavior.
  * The order affects what `super()` does.
    * This is affected by MRO (method order resolution).
    * It's possible to override behavior you did not mean to override.
