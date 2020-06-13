# Listando arquivos dentro de uma pasta 

```python
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
```

```python
# or to open and close operator 

basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
```

```python
# List all files in directory using pathlib
basepath = Path('my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)
```
