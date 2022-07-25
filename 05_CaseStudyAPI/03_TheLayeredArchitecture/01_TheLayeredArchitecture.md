# The Layered Architecture

## Why Scaffolding is useful

* Doing scaffolding in the beginning is important
  * You might realize some technical limitations early on, and you need a different library

## What is The Layered Architecture?

* We started with the data. Now we need to think about the functions.
* Layered architecture
  * Multiple layers of software. Each layer depending on the one below it.
  * 3 layers
    * Database layer
    * Operations layer
    * API routing, security, authentication layer

## Creating a layered architecture

* See code example.
* Set up operations and routers layer.
* Added a room route.

## Analysis

* DB Layer only has sqlalchemy imports
* Operations layer only has models and db imports / dependencies
* Routing layer only has dependencies to operations dependencies
