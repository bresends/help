# Como fazer 

## Gerais 
```css
h1{
    background: red;
    margin: 0; /* Pode ser negativa pra uma coisa entrar na outra */
    padding: 20px 10px 40px 20px;
    border-style: solid;
    border-width: 50px;
    border-color: green;
    border: 5px solid black;
    border-bottom-style: dashed;
    border-radius: 5px;

}
```

## Outline 
> É uma borda que pode ser deslocada com offset 
```css
h1{
    outline: 0.2rem solid #222;
    outline-offset: 10px;

}
```

# Display properties 

```css
h1{
    display: inline;
    display: inline-block;
    margin-left: auto; /* Joga todos os elementos pra direita */
    margin: auto; /* Centraliza */

}
```

# CSS Flexbox

## justify-content

* __flex-start__: Items align to the left side of the container.
* __flex-end__: Items align to the right side of the container.
* __center__: Items align at the center of the container.
* __space-between__: Items display with equal spacing between them.
* __space-around__ : Items display with equal spacing around them.

##  align-items

* __flex-start__: Items align to the top of the container.
* __flex-end__: Items align to the bottom of the container.
* __center__: Items align at the vertical center of the container.
* __baseline__: Items display at the baseline of the container.
* __stretch__: Items are stretched to fit the container.
