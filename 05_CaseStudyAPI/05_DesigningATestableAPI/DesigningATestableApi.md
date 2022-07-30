# Designing a Testable API

* We've designed an API with a layered approach.
* But if we need to turn the API for prod or to scale, we need to test it.
* A problem is that create_booking creates database sessions and it directly calls the database.
  * This makes it hard to test.
  * This makes it hard to replace the sqlalchemy library.
  * It's better to inject an object that we can replace / mock. This inverts the dependency.
* Created interfaces in db (db_interface) and operations (interface).
* Added test_bookings unit tests.
* Dependency inversion allowed us to test bookings.
* After making changes, our booking operations are no longer dependent on the Database classes.
* After making changes, our booking routers is where we connect to the database.
  * This is now the single "dirty" place where everything is configured.
