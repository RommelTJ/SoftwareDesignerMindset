# Conventions and Restrictions

When you are using mixins, there are strict conventions:   
1. Only use them to group methods. Don't add instance variables.
2. Don't create instances of mixins themselves.
3. Don't go super() inside the classes.

Mixins are useful for adding behavior to a class (as long as you follow conventions).
