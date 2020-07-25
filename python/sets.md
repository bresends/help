# Sets

## Criando set vazio
```python
x = set()
```

## Ordendando um set
```python
.sorted(variable)
```

## Adicionando Itens
```python
# Item único
x.add()

#Adicionando uma lista dentro de um set
x.update(['item1','item2','item3'])
```
## Removendo elemento de um set
```python
x.remove() 
x.discard() # não dá erro se o item não estiver na lista
```

## Criando lista com itens que estão em dois sets ao mesmo tempo
```python
lista = x.intersection(x,z)
```

## Criando lista com os valores que estão em x e não estão em y 
```python
lista = x.difference(y) # Cuidado com a ordem se é x-y ou y-x (totalmenete diferente)
```

