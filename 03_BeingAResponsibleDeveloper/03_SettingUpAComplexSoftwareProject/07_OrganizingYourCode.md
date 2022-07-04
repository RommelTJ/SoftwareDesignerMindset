# Organizing your code

* In general, avoid too generic package names, like `utils`.
  * Try to be precise with your naming.
  * Too generic names might be a code smell that you haven't thought through the design too much.
* Things that should be grouped into folders:  
  * UI code. Can be further broken down by functionality, like navigation, components, tables, etc.    
  * Operations code. The business logic for your application.  
  * Importers and Exporters code. 
  * Pages and sub-pages code. 
  * If it's an API, you might follow the structure of the API. 

