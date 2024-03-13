# Factory Method

Factory method is a creational design pattern in which we define a method for creating new objects instead of calling the `new` operator. Subclasses can override this method to change the class of objects that will be created.

In this pattern, we have an abstract `Creator` class, which is implemented by some `ConcreteCreator` classes. The abstract `Creator` class provides an abstract method to create a product, say `createProduct`, which returns the abstract `Product` type.

The `ConcreteCreator` classes implemente the `createProduct` methods and create instances of different `ConcreteProduct` classes (still, the returning type is `Product`)

This way, we can add new products without touching the client code which keeps on using the `Creator` class and the `createProduct` method. Had we directly instantiated `ConcreteProduct` in the client code, adding new products will require us to continously change client code too, thus making it open for modification. The Factory method pattern allows us to follow the open-closed principle (open for extension, closed for modification)