# Analysis of the Example

* The function `total_price` lives with the `Vehicle` class because it's close to its data.
* But it also needs information about `days` and `additional_km` that are part of `RentalContract`.
* If we look at the main function, the RentalContract needs many parameters so not ideal.
* We are also violating the Law of Demeter.
  * The main function needs to know that `rental` has a `vehicle` with a `total_price` function.
