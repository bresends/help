# Fatiando Stings 

```python
# Fatiando uma string 

a = 'Texto escrito em python'

# Selecionando de um item até um final
a[3:]

# Se selecionando do início até um item
a[:10]
```

```python
# Contando a quantidade de vezes que um caracter ocorre

a.count('o')
```

```python
# Achando a posição onde um pedaço de string começa

a.find('escrito') # Se retorna '-1' é pq não tem essa string dentro da string
```

```python
# Achando se um elemento existe ou não
'escrito' in a # Retorna um Booleano
```

```python
# Tirando os espaços à esquerda e à direita 
a.strip()
```

```python
# !!!! Gerando LISTA com as palavras de uma string !!!!
a.split()
```

```python
# Juntar palavras em uma lista pra 1 única string
'-'.join(a) # '-' é o separador usado pra juntar as palavras
```

```python
print("""
meu textão
gigante""")
```

```python
# Trocando itens
a = a.replace('Texto','Txengas')
```

# Invertendo Capitalização (maísculas e minúsculas) 
```python
# Tudo em maiúsculo ou minúsculo
a.upper()
a.lower()
a.capitalize() # apenas primeira letra maiúscula
a.title() # todas primeiras letras de uma palavra maiúsculas
```

```python
# Como colorir o print 
print('\033[1;31;43m Mensagem \033[m') #Lista das Cores Abaixo
```

```python
# Criando Prints Sucessivos sem novas linhas
print('Mensagem', end=' ')
```

[Lista das Cores](https://bixense.com/clicolors/)

# Printando Float formatado
```python
variable = 12.3

print(f'{variable:.2f}')
print(f'{variable:.5f}')
```

# Copiando dados para a área de transferência 

```python
variable = 12.3

print(f'{variable:.2f}')
print(f'{variable:.5f}')
```
