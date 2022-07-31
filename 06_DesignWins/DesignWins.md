# Design Wins

## Avoid Type Abuse

* Role is a constrained value, but we use String.
* This allows anything to be passed in.
* Constrain it to an Enum.
* In general, avoid abusing types by providing a more specific type.
* Be careful with auto naming Enums. If you alter the order, the database might get messed up. Use strings for enums.

## Use Built-In Constructs

* Roll dice method is convoluted.
* We have a for loop that goes through a range and appends to a list.
* You can do this with a built-in for-comprehension.
* Similarly, instead of summing stuff up, we can use the built-in sum function.
* Rely on built-in functions to make your code shorter and easier to maintain.

## Use Clear Names

* Contract class has an `amount` variable name that is not clear enough.
* In the example it stands for amount of hours worked, not amount of money.
* Renamed `amount` to `hours_worked`.
* By naming your variables clearly, you need less documentation.

## Avoid Flags

* Bitcoin example, with a place_order that has a flag to determine if we're buying or selling.
* Flags often indicates poor cohesion. In this case, selling and buying.
* Create separate methods for each concern. In this case, one for selling and one for buying.
* If you see a method that uses a flag, it can probably be split into multiple methods.

## Don't Use Too Many Arguments

* Room reservation example.
* Class Hotel reserve_room takes too many parameters.
* Class Reservation is a very complicated class.
* When you have a method with too many arguments, you should re-evaluate if it needs all that data.
* You can create a separate customer class to encapsulate all customer information.

## Use Shallow Nesting

* Payment example with nested if-else statements.
* Nested if-statements are often a smell for poor cohesion.
* Split each if-else into its own method.

## Avoid Deeply Nested Conditionals

## No Wildcard Imports

## Write Symmetrical Code

## Only Use Self If Needed

## Keep Classes Small

## Tell Don't Ask

## Use Meaningful Instance Variables

## Avoid Redundancy

## Don't Redefine Programming Concepts

## Protocol Segregation

## Function Composition

