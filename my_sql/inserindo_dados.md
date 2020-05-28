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
