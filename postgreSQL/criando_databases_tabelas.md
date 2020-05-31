# Criando Database

```sql
create database cadastro
default char set utf8mb4
default collate utf8mb4_unicode_ci;
```
# Apagando Database

```sql
drop database cadastro;
```

# Selecionando Database

```sql
use <nome_database>
```

# Criando tabela 

```sql
create table <nome>(
nome varchar(30)
);
```

# Apagando tabela
```sql
drop table <nome>;
```

## Garantindo ela ser única 

```sql
create table if not exists <nome>(test int);
```



Exemplo:

```sql
create type estado_civil as enum('Solteiro', 'Casado', 'Divorciado', 'Viúvo');

create table pessoas(
id bigserial not null primary key,
nome varchar(30) not null,
nascimento date,
estado_civil_pessoa estado_civil,
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar(20) default 'Brasil',
)default charset=utf8mb4;
```

# Mostrando Características das Colunas 

```sql
describe <table>;
```

# Mostrando tabela inteira
```sql
select * from <table>;
```

