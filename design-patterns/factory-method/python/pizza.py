from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self): ...

    @abstractmethod
    def bake(self): ...

    @abstractmethod
    def cut(self): ...

    @abstractmethod
    def box(self): ...


class NYCheesePizza(Pizza):
    def prepare(self):
        print("preparing ny cheese pizza...")

    def bake(self):
        print("baking ny cheese pizza...")

    def cut(self):
        print("cutting ny cheese pizza...")

    def box(self):
        print("boxing ny cheese pizza...")


class NYChickenPizza(Pizza):
    def prepare(self):
        print("preparing ny chicken pizza...")

    def bake(self):
        print("baking ny chicken pizza...")

    def cut(self):
        print("cutting ny chicken pizza...")

    def box(self):
        print("boxing ny chicken pizza...")


class ChicagoCheesePizza(Pizza):
    def prepare(self):
        print("preparing chicago cheese pizza...")

    def bake(self):
        print("baking chicago cheese pizza...")

    def cut(self):
        print("cutting chicago cheese pizza...")

    def box(self):
        print("boxing chicago cheese pizza...")


class ChicagoChickenPizza(Pizza):
    def prepare(self):
        print("preparing chicago chicken pizza...")

    def bake(self):
        print("baking chicago chicken pizza...")

    def cut(self):
        print("cutting chicago chicken pizza...")

    def box(self):
        print("boxing chicago chicken pizza...")
