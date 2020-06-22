# Capturando 
```html
<form action="..." method="...">
</form>
```
# Caixa de Entrada
```html
<input type="text" id="firstname" name="firstname">
```
# Caixa de Entrada Grande
```html
<textarea name="message" rows="10" cols="30">
The cat!
</textarea>
```

# Caixa de entrada agrupada
> Ex: First name Last name 

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

# Botões

## Regular
```html
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
```

## Bolinha
```html
// Nomes tem que ser iguais, senão ele deixa selecionar vários
<input type="radio" name="hue" id="" value="retorno"> Bolinha1
<input type="radio" name="hue" id="" value="retorno"> Bolinha2
```

## Checkbox
```html
// Nomes tem que ser iguais, senão ele deixa selecionar vários
<input type="checkbox" name="hue" id="" value="retorno"> Bolinha1
<input type="checkbox" name="hue" id="" value="retorno"> Bolinha2
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
