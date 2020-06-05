# Estrutura de um decorador básico para vários argumentos

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def print_whatever(message)
  print(message) 
```
