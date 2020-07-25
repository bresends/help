# Abertura e escrita de arquivos

```python
# Abrindo um arquivo Txt e jogando o resultado dentro de uma lista 

with open("urls.txt") as urls_file:
    for line in urls_file:
        result = get_link_count(line.strip())
        if result is not None:
            results.append(result)

results.sort(reverse=True)
```

```python
#Escrita de uma lista em um txt 

with open('arquivo.txt', 'w') as f:
  for item in lista:
    f.write(f'{item} \n')
```
