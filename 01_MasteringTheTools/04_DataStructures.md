# Data Structures

* In Python, you don't have a max integer number. It's how much memory you have available. 
* The larger your number, the more memory you need and thus the slower performance you will get.
* Integers are very precise, but not very fast. Floating points are fast, but not precise.
* The three most common data structures in python: Lists, Tuples, and Dictionaries.
* A list is a mutable, ordered sequence of items.
  * Simple to use. Grow automatically. Can be printed, sliced, appended to, etc.
  * Arrays are less flexible but are faster because they are of fixed sizes.
  * Lists are good for preserving order.
  * Lists don't work well for data that needs to be searched often.
* A dictionary maps keys to values.
  * This is good for searching.
  * Dictionaries in python are implemented as hash tables and correspond to a location in memory.
  * Search times are done in constant time.
  * Not ordered. Take more memory than lists.
* Strings in python are surrounded by quotation marks.
  * String values are immutable, but their references can be reassigned.
  * You can access strings by index.
  * Since Python 3.6 you can use f-strings to format strings.
* Enums avoid mistakes.
  * Good for representing a limited set of options.
* Tuples.
  * For when you are grouping sets of values.
  * If you need more than 2 values, probably use a class.
  * Tuples are faster to access than instance variables in an object.
  * Tuples don't provide lots of structure.
