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

## Avoid Flags

## Don't Use Too Many Arguments

## Use Shallow Nesting

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

