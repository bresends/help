# Dicionários

## Criando um dicionário

```python

# Isolado

filmes = {
    'nome':'Pulp Fiction',
    'ano': 1990,
    'genero':'ação'
}

# Dentro de uma lista

brasil = [
          {
            'Estado':'Rio de Janeiro',
            'UF': 'RJ',
            'Capital':'Rio de Janeiro'
          },

          {
            'Estado':'Minas Gerais',
            'UF': 'MG',
            'Capital':'Belo Horizonte'
          },

          {
            'Estado':'Goiás',
            'UF': 'GO',
            'Capital':'Goiânia'
          }

]
```

## Adicionando Itens

```python
dados = {'nome':'Pedro','idade':25}

#Adicionando uma 'Coluna'
dados['Sexo'] = 'M'
```

## Acessando valores individuais

```python
# Posso puxar direto
print(dict[0]['nome'])

# ou usar o método .get()
print(dict[0].get('nome'))

# Vantagem do get é que se a key não existir, ele retorna none mas não dá erro
```

# Acessando todos os valores

```python
# Keys =  Pense nelas como índices de uma tabela
print(filmes.keys())

# Values = São os valores contidos dentro das keys
print(filmes.values())

# Items = Soma de cada par de key e value de um dicionário
print(filmes.items())
```

## Modificando valores

### Individuais

```python
dict[0]['nome'] = 'Maria'
```
### Vários ao mesmo tempo

```python
dict[0].update({'nome':'Tião', 'idade':'55'})
```

## Removendo valores

```python
del dados['idade']
```

## Fazendo Loops em Dicionários

```python
# Mostrando todos os items (que são a combinação dos valores de keys e values juntos)

for k,v in filmes.items():
  print(f'A key [{k}] tem como valor [{v}]')

# Mostrando apenas os keys de um dicionário
for k in filmes.keys():
  print(k)

# Mostrando apenas os values de um dicionário
for v in filmes.values():
  print(v)

```

## Dictionary Comprehension

```python
# Multiplicando Valores por 2
double_dict1 = {k*2:v*2 for (k,v) in dict1.items()}

# Filtrando valores
new_dict = {key: value for key, value in a_dict.items() if value <= 3 if value > 1 }
```

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

