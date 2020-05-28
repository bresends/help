# GIT Local

## Criando Repositório dentro de uma pasta
```bash
git init
```

## Mostrando o que mudou no projeto
```bash
git status
```

## Commit
```bash
git commit -am "Comentário" 
```

## Mostrando histórico dos commits

```bash
git log
```

## Retornando a uma versão anterior (pra olhar) 
```bash
git checkout <hash_commit>
```

## Voltando tudo pro último commit
```bash
git checkout master
```

## Retornando em definitivo para um commit anterior
```bash
git reset --hard <hash_commit>
```

## Criando Branch
```bash
git checkout -b <nome_branch>
```
## Mostrando branch onde estamos trabalhando
```bash
git branch
```

## Fazendo merge de um Branch
```bash
# Estando no Master
git merge <nome_do_branch> 
```
