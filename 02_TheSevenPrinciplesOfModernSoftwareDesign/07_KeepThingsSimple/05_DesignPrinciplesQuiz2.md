# Design Principles Quiz 2

Q: Below you find several statements related to the Start With The Data principle. Which of these are true?    
A: You should generally put a method in the class that contains most of the data this method needs.  
A: You can achieve separation between creation and use without relying on abstractions.

Q: John has written a function to generate a random id.
   Currently, this function is only used to generate ids containing numbers. 
   Just to be sure, John also added functionality for (uppercase) characters, symbols, as well as several 
   standardized id formats such as GUID and WPA keys. What principle did John violate?  
A: YAGNI.

Q: Rachel has written a function to compute the circumference of a circle. 
   The radius of the circle is not provided by a parameter, but by a StreamInterface, so you can potentially 
   retrieve the radius value over a network connection, read it from a file, retrieve it from a database, 
   and so on (though she didn't implement any of those). Which principle did Rachel violate?  
A: KISS.

Q: Arjan has written a function that reads various pieces of information from a file. 
   The function is quite long because the code for reading each piece of information is very similar. 
   What principle did Arjan violate?  
A: DRY.

Q: Which of the following is an example of dependency injection?  
A: A method in class A uses an object of type B that it receives as an argument.  

Q: "You can't have dependency inversion without dependency injection". True or false?  
A: True.
