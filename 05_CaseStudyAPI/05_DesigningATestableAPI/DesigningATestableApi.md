# Designing a Testable API

* We've designed an API with a layered approach.
* But if we need to turn the API for prod or to scale, we need to test it.
* A problem is that create_booking creates database sessions and it directly calls the database.
  * This makes it hard to test.
  * This makes it hard to replace the sqlalchemy library.
  * It's better to inject an object that we can replace / mock. This inverts the dependency.
