# Adicionando Foreign Key

```sql
alter table <table>
add column <nome_nova_coluna> <tipo>; # Cuidado. Tem que ser exatamente do mesmo tipo que a foreign key

alter table <table>
add foreign key (<Nome_nova_coluna>)
references <tabela_externa>(<coluna_externa_referenca>);
```

# Referenciando isso na tabela

```sql
update <table> set <nome_nova_coluna> = '<valor>' where <nome_coluna_exterior> = '<valor>'
```

# Fazendo Join (mostrar informações de uma tabela na outra

```sql
select <tabela_com_a_relação>.<coluna_desejada1>, <tabela_extrangeira>.<coluna_desejada2>
from <tabela_com_a_relação> inner join <tabela_extrangeira>
on <tabela_extrangeira>.<coluna_relação> = <tabela_com_a_relação>.<coluna_relação>
```

# Relacionamento n pra n (muito pra muitos)

Nesse caso eu tenho 2 tabelas que se relacionam e cada chave de cada uma pode assumir várias chaves na outra
Ex: Alunos e Cursos (cada aluno assiste vários cursos e cada curso é assitido por vários alunos)
É necessário que eu construa uma tabela pra fazer um relacionamento 1 para n pegando esses 2 valores

```sql
create table aluno_assiste_curso(
id int not null auto_increment,
data date,
idaluno int,
idcurso int,
primary key (id),
foreign key (idaluno) references aluno(id),
foreign key (idcurso) references curso(id)
```

## Fazendo Join
