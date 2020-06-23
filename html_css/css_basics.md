# Selecionando itens 

## ID (devem ser únicos)

```css
#nomeid {
    color: blue;
}
```

## Classe (devem ser usados para quando vários elementos tem os mesmos atributos)
```css
.nome_classe {
    color: blue;
}
```

# Atributos interessantes 
```css
div {
    text-transform: uppercase;
    text-aligment: center;
    text-indent: 50px; /* Tamanho do parágrafo */
    line-height: 1em;
    letter-spacing: 5px;
    word-spacing: 5px;
    text-decoration: underline; /* Tira pro exemplo o underline dos links */
    text-decoration: none; /* Tira pro exemplo o underline dos links */
    border: 3px solid black;
}
```


# Tamanhos
```css
div {
    font-size: 30px; /* Tamanho absoluto */
    font-size: 30%; /* Tamanho relativo à classe mãe (tem que estar dentro dela) */
    font-size: 2em; /* Tamanho Relativo à classe mãe */
    width: 50vw; /* Responsivo ao tamanho EXATO da tela */
    height: 5vh;
    min-height: 15vh; /* Se tamanho do elemento for menor que esse valor ele se mantém */
    min-height: calc(100px - 15vh); /* Faz conta pra fazer coisas se encaixarem no que for necessário */

}
```

# Margens

## Tirando margens do navegador

```css
/* Elemento mãe do DOM */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

## Fazendo lista mas sem os pontos 
```css
/* Elemento mãe do DOM */
ul li {
    list-style-type: none;
}




