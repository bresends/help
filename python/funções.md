# Funções Regulares

## Criando Função sem quantidade definida de variáveis 

```python
def contador(*num):
  print(num)
  print(f'A sua função tem {len(num)} itens')
```

# Funções Lambda

> Lógica: __lambda__ recebe __x__ retona __x*x__

```python
# Fazendo sort de uma lista dentro de lista pelo segundo elemento 

lista = [
    ['Batata', 13],
    ['Maça',15],
    ['Carne', 22],
    ['Milho', 3]
]

# Usando lambda para selecionar o item
lista.sort(key=lambda item: item[1])
```
