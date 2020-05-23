# Listas

## Adicionando itens 

```python
# No fim
lanche = ['pão', 'pudim', 'broa']
lanche.append('bolo')

# Em posição específica
lanche.insert(0,'pão de queijo') # dá a posição e depois o item a ser adicionado
```

## Adicionando uma lista dentro de outra lista, mas como elementos individuais, não outra lista

```python
# Assim joga a lista
sobremesa = ['sorvete']
sobremesa.append(lanche)

# Assim joga só os valores
sobremesa = ['sorvete']
sobremesa.extend(lanche)
```

## Apagando itens
```python

# Aqui ele vai na lista e remove o item que vc desejar (independente da posição do mesmo)

lanche.remove('broa')

# Checando se o item está na lista antes de apagar pra não dar erro
if 'pudim' in lanche:
  lanche.remove('pudim')
```

## Apagando itens
```python
# Pop
lanche.pop(0) #se estiver sem o índice, ele remove o último elemento da lista

# Del
del lanche[0]
```

# List Compreehension

> Lógica: ``` [(x*x) for x in lista] ```

```python
# Fazendo replace em uma string
lista_atualizada = [item.replace('u','Txnchegas').replace('a','@').upper() for item in lista_nomes]
```

```python
# Listando todos os números divisíveis por 3 e 8 ao mesmo tempo 

lista_item = list(range(100))

lista_filtrada = [(item) for item in lista_item if item % 3 == 0 if item % 8 == 0]
```

```python
# Aplicando função
# Lista
prices = [1.09, 23.56, 57.84, 4.56, 6.78]

def discount(item):
    return item * (0.9)

final_prices = [discount(i) for i in prices]
```

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

