# Alterando 

## Alterando 1 valor de 1 linha

```sql
update <table>
set <column>='Valor a ser alterado'
where <tabela_referencia>=valor_referencia'
limit 2;
```

>Exemplo
```sql
update cursos
set nome='Java', ano=2015
where idcurso='5';
```

Cuidado. Se o 'where' não for único, ele vai mudar tudo.
Pra isso vc pode dizer ```limit 1```;

# Deletando 

## Deletando linhas

```sql
delte from <table>
where <tabela_referencia>='valor_referencia'
limit 1;
```

## Apagando todas as linhas

```sql
truncate <table>;
```
