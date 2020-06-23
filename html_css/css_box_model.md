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

```css
div{
    display: flex;
    
    justify-content: flex-start; /* Items align to the left side of the container. */
    justify-content: flex-end; /* Items align to the right side of the container. */
    justify-content: center; /* Items align at the center of the container. */
    justify-content: space-between; /* Items display with equal spacing between them. */
    justify-content: space-around; /* Items display with equal spacing around them. */
   
}
```

##  align-items

```css
div{
    display: flex;
    
    align-items: flex-start; /* Items align to the top of the container. */
    align-items: flex-end; /* Items align to the bottom of the container. */
    align-items: center; /* Items align at the vertical center of the container. */
    align-items: baseline; /* Items display at the baseline of the container. */
    align-items: stretch; /* Items are stretched to fit the container. */
   
}
```

## flex-direction

div{
    display: flex;
    
    flex-direction: row; /* Items are placed the same as the text direction. */
    flex-direction: row-reverse; /* Items are placed opposite to the text direction. */
    flex-direction: column; /* Items are placed top to bottom. */
    flex-direction: column-reverse; /* Items are placed bottom to top. */
   
}


