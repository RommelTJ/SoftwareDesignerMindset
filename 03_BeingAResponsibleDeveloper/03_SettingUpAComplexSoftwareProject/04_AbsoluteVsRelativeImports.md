# Absolute vs Relative Imports

* An absolute import is one that includes the full package path.
  * Ex: `from package_1.file_2 import file_2_function`
* A relative import is one that is relative to the file doing the importing.
  * Ex: `from .file_1 import file_1_function`
  * The number of dots indicates how many levels up you go in the package hierarchy.
