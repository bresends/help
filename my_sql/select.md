# Filtrando todos os registros de todas as colunas
```sql
select * from <table>
```

# Ordenando linhas por coluna específica
## Ascendente
```sql
select * from <tabela>
order by <nome_coluna_1>, <nome_coluna_2>;
```
## Descendente 
```sql
select * from <tabela>
order by <nome_coluna> desc;
```

# Filtrando Colunas
```sql
select <coluna_1>, <coluna_2> from <tabela>
order by <nome_coluna>;
```

# Filtrando linhas
```sql
select * from <table>
where <coluna_controle> <= 'Critério';
```

# Operadores relacionais e Lógicas

## Entre um valor e outro
```sql
select * from <table>
where <coluna_controle> between 'Critério1' and 'Critério2';
```

## Dentro de uma lista de parametros
```sql
select * from <table>
where <coluna_controle> in ('Critério1', 'Critério2', 'Critério3');
```

# And
```sql
select * from <table>
where <coluna_controle1> < 'z' and <coluna_controle2> > 'y';
```

# Like
# Selecionando apenas os que começam com P

```sql
select * from <table>
where <coluna_controle1> like 'P%';
```

# Selecionando as palavras que não tenham a letra A (qualquer posição)
```sql
select * from <table>
where <coluna_controle1> not like '%A%';
```

# Mostrando apenas values únicos
```sql
select <coluna> distinct from <table>;
```

# Funções de agregação

## Mostrando quantos elementos tem dada uma condição
```sql
select count(*) from <table> where <column> > 'z';
```

## Mostrando máximo/mínimo/sum/avg
```sql
select max(<coluna>) from <table>;
```

## Com nome
```sql
select <coluna_nome> max(<coluna>) from <table>;
```

## Agrupando Registros (GroupBy)

```sql
select <coluna> from <table>
group by <coluna>;
```

## Agrupando com condicionais
```sql
select <column>, count(<column_for_count>) from <table>
group by <column>
having count(<column_for_count>) > 'z';
```

Exemplo
```sql
select nacionalidade, count(nacionalidade) from gafanhotos
where nacionalidade != 'Brasil'
group by nacionalidade
having count(nacionalidade) > '3'
order by nacionalidade;
```

## Contando quantidade de registros únicos 

```sql
select <coluna>, count(*) from <table>
group by <coluna>
order by <coluna>
```




