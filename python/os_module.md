# Listando arquivos dentro de uma pasta 

```python
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
```

```python
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files("."):
    print (file)
```
