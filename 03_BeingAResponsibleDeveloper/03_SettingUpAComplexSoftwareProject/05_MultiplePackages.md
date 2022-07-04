# Multiple Packages

* You can add multiple packages to a project.
  * You can add a sub-package to a package.
* Packages in Python can use each other.
  * You might want to limit that, though. Packages are supposed to be independent.
  * Preferably, each package is as independent as possible.
* Relative imports are not possible in packages.


```python
from package_1.file_2 import file_2_function
from package_2.sub_package.file_4 import file_4_function
```
