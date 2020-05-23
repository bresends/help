# Adicionando itens 

```python
# Adicionando item em uma lista no final (Posso por uma lista também)
lanche = ['pão', 'pudim', 'broa']
lanche.append('bolo')


# Adicionando item em uma lista num lugar específico 
lanche.insert(0,'pão de queijo') # dá a posição e depois o item a ser adicionado
```

```python
# Adicionando uma lista dentro de outra lista, mas como elementos individuais, não outra lista

# Assim joga a lista
sobremesa = ['sorvete']
sobremesa.append(lanche)
print(sobremesa)

# Assim joga só os valores
sobremesa = ['sorvete']
sobremesa.extend(lanche)
```

```python
## Apagando pelo conteúdo ##
# Aqui ele vai na lista e remove o item que vc desejar (independente da posição do mesmo)

lanche.remove('broa')
print(lanche)

# Checando se o item está na lista antes de apagar pra não dar erro
if 'pudim' in lanche:
  lanche.remove('pudim')
```

```python
## Apagando pelo índice ##

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
print(final_prices)
```

# Dicionários

## Criando um dicionário
```python
filmes = {
    'nome':'Pulp Fiction',
    'ano': 1990,
    'genero':'ação'
}
```

## Acessando valores individuais
```python
# Posso puxar direto
print(pessoas_dict[0]['nome'])

# ou usar o método .get()
print(pessoas_dict[0].get('nome'))

# Vantagem do get é que se a key não existir, ele retorna none mas não dá erro
```

