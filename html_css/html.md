# Imagens

> * O uso do Style não deixa o CSS mudar o tamanho. 
>  * Pode usar GIF também 
```html
<img src="html5.gif" alt="HTML5 Icon" width="128" height="128">
<img src="/images/html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">
<img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com">
```
O alt serve pra quando a imagem não carregar, ele mostrar qual o nome (pra quando der err) 

# Links 

## Abrir em nova janela 

```html
<a href="https://www.udemy.com" target="_blank"> Visit </a>
```

## Retornando a um elemento 
```html
<h1 id="top">Top of Page </h1>
<br>
<br>
<a href="#top"> Back to the Top </a>
```

## Links dentro de Imagens
```html
<a href="https://www.udemy.com">
  <img src="images/imagem.txt" alt="doguinho" width="200">
</a>
```

# Listas 
## Com ordem 
```html
<ol>
  <li> Peter </li>
  <li> Sara </li>
  <li> Whatever </li>
</ol>
```

## Sem ordem 
```html
<ul>
  <li> Peter </li>
  <li> Sara </li>
  <li> Whatever </li>
</ul>
```

# Tables
>Each table row is defined with a <tr> tag. Each table header is defined with a <th> tag. Each table data/cell is defined with a <td> tag.

```html
<table>
    <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
        <td>45</td>

    </tr>
    <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
    </tr>
</table>
```

# Formulários

## Caixa de Entrada
```html
<input type="text" id="firstname" name="firstname">
```
## Caixa de Entrada Grande
```html
<textarea name="message" rows="10" cols="30">
The cat!
</textarea>
```

# Caixa de entrada de diversos elementos semelhantes

```html
<form action="/action_page.php">
  <fieldset>
    <legend>Personalia:</legend>
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname" value="Doe"><br><br>
    <input type="submit" value="Submit">
  </fieldset>
</form>
```

## Botões
```html
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
</textarea>
```


# Menu 
```html
<select id="cars" name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="fiat">Fiat</option>
  <option value="audi">Audi</option>
</select>
```


# Formatação 
## Sobrescrito e Subscrito 
```html
<p> Hi <sup> 1st </sup> and Hi <sub> 1st </sub></p>
```
## Negrito e Itálico
```html
<p> Hi <strong> 1st </strong> and Hi <emp> 1st </emp> </p>
```

## Caracteres especiais 
```html
<p> copyright &copy; </p>
```
