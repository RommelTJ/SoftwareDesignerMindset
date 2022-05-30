# Data Structures Quiz

1. What's the largest possible value that Python's int type can store?  
A: There is no largest value - the int type dynamically adapts the memory it needs

2. What's the best built-in type in Python to use for representing monetary amounts?  
A: int

3. Why is int better suited for representing monetary values than float?  
A: The float type is not precise enough for representing monetary values.

4. What happens when you try to add a float and an int in Python?  
A: The result is computed and is of type float.

5. What do we mean if we say that a type is mutable?  
A: Objects of a mutable type are allowed to change their value.

6. Consider the following lines of code:
```python
my_list = [0, 2, 4, 6, 7, 5]
new_list = my_list[4:] + my_list[:2]
```
What's the value of new_list?  
A: [7, 5] + [0, 2] = [7, 5, 0, 2]

7. For a web scraping project, you need to cache search results based on keywords. What's the most suitable data 
structure to store these cached results in?  
A: dict

8. An image processing pipeline needs a data structure to represent the sequence of processing operations to be 
performed on a particular image. What's the best data structure for this?  
A: list

9. The function `connect_to_database` can setup a connection to a database of choice, and it returns a `Connection` 
object with which you can access the database as well as a `ConnectionResult` object that contains information about 
the kind of connection that was established. What's the most suitable data structure for containing these two objects?  
A: tuple

10. A profanity filter has a collection of profane words that it uses to filter user messages. What's the most 
suitable data structure for this word collection?  
A: set

11. I want to build a system where, given a customer's (unique) email address, I can quickly retrieve the customer 
information. I already have a class `Customer` that contains all that information (including the email address). 
What's the most performant approach?  
A: Create a dict[str, Customer] and use the email address as a key
