# Abstract Factory

- Resource: https://refactoring.guru/design-patterns/abstract-factory
- Abstract Factory is a creational design pattern, which lets us create families of related objects without specifying their concrete classes.
- For example, suppose your client wants a sports kit (which includes products like shoe, shirt, etc). Sports Kit can be of different brands, but anyone buying a sports kit would want that everything they buy is of the same brand. (Shoe of Adidas and Shirt of Nike won't look consistent).
- But, we don't want our clients to keep bothering about the brand of every product all the time. They just tell us once that we want a sports kit of this brand, and then every time they ask for something, we give them a product from the same brand even if they don't specify the brand. All they care about is a Shoe (or a Shirt).
- Such a case can be solved using Abstract Factory pattern.

- We create an abstract factory interface called `ISportsFactory`, which defines methods `makeShoe` and `makeShirt`.
- We create concrete factories, say `AdidasFactory` and `NikeFactory`. These factories implement the methods `makeShoe` and `makeShirt`. But, the signatures of these methods involve only the interface types `IShoe` and `IShirt`, even though they actually return objects of types `AdidasShoe` or `NikeShirt`, etc.