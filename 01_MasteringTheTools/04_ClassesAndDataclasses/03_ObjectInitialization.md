# Object Initialization

* Dataclasses support default values at initialization.
* Dataclasses don't allow initialization to an empty list.
  * A list is a mutable object, so it's not allowed to provide mutable objects for a default.
  * But you can still do it by using the "field" function with a default_factory.
