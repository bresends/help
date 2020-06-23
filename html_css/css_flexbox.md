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

```css
div{
    display: flex;
    
    flex-direction: row; /* Items are placed the same as the text direction. */
    flex-direction: row-reverse; /* Items are placed opposite to the text direction. */
    flex-direction: column; /* Items are placed top to bottom. */
    flex-direction: column-reverse; /* Items are placed bottom to top. */
   
}

```

## wrap 


```css
div{
    display: flex;
    
    flex-wrap: nowrap; /* Every item is fit to a single line. */
    flex-wrap: wrap; /* Items wrap around to additional lines. */
    flex-wrap: wrap-reverse; /* Items wrap around to additional lines in reverse. */
   
}

```
