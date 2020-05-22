# Conda Virtual Environments 

```
#Criando 
conda create -n nomes_ambiente python=3.8
```

```
# Ativando 
activate nome_ambiente
```

```
# Mostrando os pacotes do ambiente
conda list
```

```
# Mostrando todos os ambientes
conda env list 
```

```
# Saindo do ambiente 
deativate nome_ambiente
```

```
# Deletando 
conda env remove -n nome_ambiente
```

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

# Browser 

```python
# Abrir url em nova janela 

import webbrowser
webbrowser.open('http://example.com')

```

# Tratamento de Erros 

```python
# Divisão por zero 

try: # Aqui eu digo o que é pra ele tentar
  a = 1
  b = 0
  r = a/b

except Exception as erro: # Aqui o que é pra ele fazer se der erro / Nesse caso pegando todos os erros. Pode ser feito individual
  print(f'{erro} - Não dá pra dividir por zero ')

else: # Opcional: o que ele deve continuar fazendo se der tudo certo
  print('Belezinha')
  print(r)

finally: # Opcional: O que o programa deve fazer independente de dar certo ou dar errado
  print('Obrigado por usar o programa')
```
