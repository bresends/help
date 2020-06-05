# Estrutura de um decorador básico para vários argumentos

```python
def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

@decorator
def function_to_be_decorated(args)
  pass
```

# Decorador com captura de retorno da função 

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```
