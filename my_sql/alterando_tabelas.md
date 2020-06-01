## Adicionando Colunas

### Adicionando Coluna na última posição
```sql
alter table <table>
add column varchar(30);
```

### Adicionando Coluna em uma posição específica
```sql
alter table <table>
add column varchar(30) after <outra_coluna>;
```

### Adicionando Coluna na primeira coluna
```sql
alter table <table>
add <column> <type: e.g. int> first;
```


## Removendo Coluna
```sql
alter table <table>
drop column <coluna>
```


## Renomeando coluna
```sql
ALTER TABLE <nome_tabela>
RENAME COLUMN <column_name> TO <new_name>;
```

## Mudando tipo de dado na coluna 

```sql
alter table <table>
modify column <coluna> varchar(20);
```

## Selecionando coluna como primary key 

```sql
alter table <table_name>
add primary key(<nome_coluna>);
```

## Mudando nome da tabela

```sql
alter table <tabela>
rename to <new_name>;
```
