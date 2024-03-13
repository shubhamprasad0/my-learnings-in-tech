from abc import ABC, abstractmethod
from .pizza import (
    Pizza,
    NYCheesePizza,
    NYChickenPizza,
    ChicagoCheesePizza,
    ChicagoChickenPizza,
)


class PizzaStore(ABC):
    def order_pizza(self, type: str) -> Pizza:
        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type: str) -> Pizza: ...


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        if type == "cheese":
            return NYCheesePizza()
        elif type == "chicken":
            return NYChickenPizza()


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        if type == "cheese":
            return ChicagoCheesePizza()
        elif type == "chicken":
            return ChicagoChickenPizza()
