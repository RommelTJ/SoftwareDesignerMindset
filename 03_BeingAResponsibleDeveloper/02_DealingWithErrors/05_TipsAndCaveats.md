# Tips and Caveats

* Don't focus too much on putting try-catch everywhere.
* Only do so if you have a good reason.
* Sometimes it's ok to end the application with an error.
* Keep it simple principle.
* Don't catch a generic exception. It's too broad.
  * In particular with Python, this is problematic since the compiler relies on exceptions being thrown.
