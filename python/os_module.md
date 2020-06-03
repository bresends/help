# Listando arquivos dentro de uma pasta 

```python
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
```
