# Usando triggers no HTML para Javascript 

> Devo criar uma função em Javascript e colocar o trigger no html 

```html 
<script>
  function nome_funcao() {
    comandos desejados
  }
</script>

<h1 onclick='nome_funcao()'> Texto </h1>
```

# Eventos 

```html
onclick=''
onmouseover='' // Mouse passa em cima 
onmouseout='' // Mouse sai 
onmousedown='' // Botão esquerdo pressionado 
onmouseup='' // Botão esquerdo solto após pressionado
onload='' // Quando página termina de carregar 
```

# Pegando os elementos 

## por Tag
```javascript
let paragraph = window.document.getElementsByTagName('p')[0]
```

// Printando Texto sem formação 
```javascript
window.document.write(paragraph.innerText)
```
// Printando Texto com formatação
```javascript
window.document.write(paragraph.innterHTML)
```

// Mudando cor
```javascript
paragraph.style.color = 'blue'
```

## por ID
```javascript
let a = window.document.getElementById('nome_id')
a.innerText = 'Nova String'
```
## por Nome
```javascript
window.document.getElementsByName()
```
## por Classe
```javascript
window.document.getElementsByClassName()
```
## por Seletor (mais moderno e mais recomendado) 
```javascript
// Um elemento
let d = window.document.querySelector('div#id')
let d = window.document.querySelector('div.class')

// Vários elementos 
let d = window.document.querySelectorAll('div#id')

// Mudando atributos
d.style.background = 'blue'
```




