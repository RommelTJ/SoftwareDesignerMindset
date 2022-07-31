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

* Nested conditionals are really hard to understand.
* Use simple if statements.

## No Wildcard Imports

* Wildcard imports make it really hard to understand where something comes from.
* Wildcard imports can also easily lead to name clashes.
* Wildcard imports makes it easy to make mistakes, and introduces a lot of coupling.
* Regular imports make it clear where stuff comes from. Use regular imports.

## Write Symmetrical Code

* Equipment rental example.
* PowerDrill and CementMixer calculate rental price differently.
* This is a bad idea because if we want to rent both, you have to worry about renting them correctly.
* Increase consistency by bringing things in line with each other.
* If you have full control over the code, update it.
* If you don't have full control over the code, use the adapter pattern.

## Only Use Self If Needed

* If a method doesn't need self, turn it into a static method instead.

## Keep Classes Small

* A Player class with a lot of instance variables.
* If you have this scenario, ask if it's really necessary? Can you split the behavior?
* In the example, we split the instance variables into Character traits and personal traits.

## Tell Don't Ask

* Normalize function gets a vector and then calculates over its values.
* Turned the function into an instance method.
* Now we tell the vector what to do. Don't retrieve all kinds of information and calculate data from that.

## Use Meaningful Instance Variables

## Avoid Redundancy

## Don't Redefine Programming Concepts

## Protocol Segregation

## Function Composition

