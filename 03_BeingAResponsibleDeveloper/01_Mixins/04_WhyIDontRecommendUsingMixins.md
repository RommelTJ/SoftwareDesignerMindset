# Why I don't recommend using Mixins

* Typing systems don't know what to do with mixins.
  * Since you get type errors, they are not so useful when you use the type hints.
  * You can avoid that by disabling the errors, but then you can get bad errors.
* The only way to use it properly is to limit Object-oriented features.
  * See conventions and restrictions.
  * Teammates might not know conventions and mess things up.
  * Makes team collaboration harder.
* Mixins potentially interfere with other things.
  * Ex: dataclass are used a lot. Can we use mixins with dataclasses? Who knows?
  * Suppose you need an instance variable. Now you need to refactor around the mixins.
  * Inheritance can get broken. They are no longer is-a relationships.
