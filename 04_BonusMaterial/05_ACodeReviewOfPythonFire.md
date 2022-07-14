# A Code Review of Python Fire

* Code reviewing the python-fire library
  * Python Fire is a library for automatically generating command line interfaces (CLIs) from 
    absolutely any Python object
* Structure
  * No structure whatsoever. Everything is in the same folder.
  * Makes it hard to know where to start the code review.
  * Prefer to keep the test files separate from the main code.
* Naming conventions are not followed.
* No type hints.
* Functions that are 600+ lines long.
* Don't put TODOs in code. They're very hard to find. They stay in your code forever.
* Google developers don't always listen to their style guide.
* Presence of many if-else statements are candidates to refactor to Strategy pattern or dictionary.
