# Importação das Bibliotecas

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

# Abrindo, fechando e maximizando o navegador

```python
# Instanciando 
driver = webdriver.Chrome('./chromedriver')

# Fechando navegador
driver.quit()

# Fechando Guia
drive.close()

# Minimizando e maximizando 
driver.maximize_window()
driver.minimize_window()
```

# Abrindo uma página

```python
driver.get('http://google.com.br')
```

# Capturando Informações

```python
# HTML da página toda
drive.page_source
```

```python
# Título da página
drive.title
```

```python
# URL da página atual 
driver.current_url
```

# Navegando na página

## Pra frente e pra trás

```python
driver.back()
driver.foward()
```
## Clicando em um item

```python
driver.find_element_by_xpath('//*[@id="ctl00_mainContent_txtLogin"]') # Tem que trocar as double cotes por singles
```

## Preenchendo formulários

```python
driver.find_element_by_xpath('//*[@id="ctl00_mainContent_txtLogin"]').send_keys('brunoresende')
```

## Rolando na página

```python
# Um tanto de pixels 
driver.execute_script("window.scrollBy(0,500)","")

# Até um elemento selecionado 
elemento_na_pagina = driver.find_element_by_xpath("...")
driver.execute_script("arguments[0].scrollIntoView();", elemento_na_pagina)

# Até o fim da página 
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
```

# Verificando existência de um elemento na página

```python
# Idenfica o elemento
element = driver.find_element_by_name("userName")

# Verifica presença
element.is_displayed() # Retorna booleano se o elemento está sendo mostrado
element.is_enabled()
```

# Encontrando elementos 

```python
find_element_by_id('<id>')
```

```python
find_element_by_name('<name>')
```

```python
find_element_by_link_text('<text>')

```

```python
find_element_by_css_selector('<css_selector>')
```

```python
find_elements_by_tag_name('<tag_name>')
```

```python
find_elements_by_class_name('<class_name>')
```
