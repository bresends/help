# Inserindo dados na tabela

## Valor único
```sql
insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
('1', 'Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil');
```

## Múltiplos valores
```sql
insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
('1', 'Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil'),
('2', 'Hudosvaldio', '1978-08-02', 'M', '78.5','1.83', default');
```

## Lista estando na ordem

```sql
insert into pessoas values
(default,'Adalgiza', '1999-12-30', 'F', '55.2','1.65','Portugal');
```

# Alterando Dados 

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
alter table pessoas
change <column_name> <new_name>;
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
