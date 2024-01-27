# Exception Handling

## `try, except, else, finally`

```python
try:
    # Run this code
    ...
except:
    # Run this if an exception occurs
    ...
else:
    # Run this if no excpetion occurs
    ...
finally:
    # Always run this code in the end
    ...
```

## Define custom exceptions

```python
class MyCustomException(Exception):
    pass
```