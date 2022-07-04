# Import Tips

* In Python, you can use a wildcard to import everything.
  * Ex: `from package_1.file_1 import *`
* Avoid wildcard imports.
  * If you have many of them, it pollutes the namespace.
  * It becomes hard to know which functions belong to which modules.
* Always make clear where functions are coming from.
* You can also use import name aliases.
  * Ex: `from package_1 import file_1 as f1`
  * Ex: `import numpy as np`

