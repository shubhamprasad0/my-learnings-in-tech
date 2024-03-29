# Decorators

## Study Material 

- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

## Notes

- **Decorator:** A function which takes another function as argument and extends its behaviour without explicitly modifying it. Decorators wrap a function to extend its behaviour.
- In python, functions are first class objects, which means they can be treated like normal objects in python. They can be passed around as function arguments, and they can be returned from functions.
- **Decorators on methods of class:** Some in-built decorators are `@classmethod`, `@staticmethod`, `@property`
- **Decorators on class:** E.g. `@dataclass`

    ```python
    from dataclasses import dataclass

    @dataclass
    class PlayingCard:
        rank: str
        suit: str
    ```


