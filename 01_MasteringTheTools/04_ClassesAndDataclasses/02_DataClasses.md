# Data Classes

* Data Classes provide a basic implementation of a data-oriented class and removes boilerplate code.
  * You can make a field uninitializable by adding init=False to the field value.
  * If you don't want to use a default_factory, you can also remove the default_factory but add a post_init dunder method
  * You can add `@dataclass(frozen=True)` to prevent a class from being modified
