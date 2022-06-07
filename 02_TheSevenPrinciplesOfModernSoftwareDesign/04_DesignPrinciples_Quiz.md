# Design Principles Quiz 1

Q: Why is composition favored over inheritance?  
A: It simplifies your original design. It avoids a combinatorial explosion of subclasses that represent 
traits instead of being real extensions. It more easily accommodates future changes in requirements.

Q: True or false: you cannot do composition without inheritance?  
A: False.

Q: Which levels of cohesion and coupling are generally desirable?  
A: High cohesion, low coupling.

Q: What level of cohesion does the following code have?  
A: Low cohesion.

Q: What level of cohesion does a function like log(x) or sqrt(x) have?  
A: High cohesion.

Q: What do you call the type of coupling where a class directly reads or changes a variable of another class?  
A: Content coupling.

Q: Suppose you have two functions project_to_viewport and capture_screen_shot that both rely on 
globally defined constants VIEWPORT_WIDTH and VIEWPORT_HEIGHT. What type of coupling do these two functions have?  
A: Global coupling.

Q: Which of the cases below is an example of breaking the Law of Demeter?  
A: A method in class A accesses an object C which is a property of object B, and calls a method on it.

Q: Data coupling can be eliminated by...?  
A: Employing message passing.

Q: Consider a hierarchy of Shape classes and subclasses. The Shape class is given as follows:  
Here's an example of a Shape subclass, Rectangle:  
Next to different Shape subclasses, there's a Parser class that reads shapes from a file and returns a list of shapes.
There's also a ShapeDisplay class that's responsible for drawing the shapes and displaying information about them.
Suppose you want to extend the functionality of the shapes to be able to compute and show the perimeter. Which 
classes need to be changed?  
A: The Shape class, its subclasses and the ShapeDisplay class.
