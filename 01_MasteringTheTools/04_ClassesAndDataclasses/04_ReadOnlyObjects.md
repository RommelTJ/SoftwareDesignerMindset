# Read-Only Objects

* You can make an object read-only by marking it as `@dataclass(frozen=True)`
* Encapsulation helps to separate code better. Less coupling of your code.
  * Data Classes encourages coupling because it allows you access to instance variables.
  * Python has an unwritten convention with "_" that makes a variable private.
