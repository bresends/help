# Grid

## Criando o grid

>Crio uma super class pra abrigar meus elementos dou quantas colunas e o tamanho de cada uma

```css
display: grid;
grid-template-columns: 100px auto 100px; /* Criando 3 colunas com a do meio ajustando */
grid-template-columns: 1fr 2fr 1fr; /* Criando 3 colunas com a do meio sendo o dobro sendo todas responsivas */
grid-template-columns: repeat(3, 1fr); /* Criando 3 colunas de mesmo tamanho responsivas */
grid-template-rows: 50px 50px;
grid-gap: 3px;  /* Distância entre cada um dos elementos */
```

## Posicionando itens (header completo, com menu lateral menor e content)
```css
.container {
    display: grid;
    grid-gap: 3px;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: 40px 200px 40px;
}

.header {
    grid-column: 2 / -1;
}

.menu {
    grid-row: 1 / 3;
}

.content {
    grid-column: 2 / -1;
}

.footer {
    grid-column: 1 / -1;
}
```

## Fazendo imagem se ajustar no grid 

```css
.container > div > img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```