# Comandos Importantes 

```python
# Achar texto 
soup.body.findAll(text='Python')
```

```python
# Achar classe CSS e pegar valor de elemento
soup.find_all('p', class_='data lastcolumn')[30].get_text()
```

```python
# Achar HTML e pegar valor de elmento
soup.h2.get_text()
soup.title.get_text()
```

```python
# Pra ver o elemento tem que dar print no prettify 
print(bs4_obj.prettify())
```

# Manipulando Dados 

```python
# HTML 
stock = soup.h2.get_text()
```

```python
# CSS
sector = soup.find_all("span", class_="descricaoaba")[0].get_text()
```

```python
# Remover classes de dentro de uma tag
last_links = soup.find(class_='descricaoaba')
last_links.decompose()
```
