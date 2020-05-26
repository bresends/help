# Instalação

>Instalar o vs code antes. 
>Desmarcar o gui, selecionar a versão correta do VS Code
>Git from command line and 3rd Party

# Configuração Inicial
```bash 
git config --global user.name "Bruno"
git config --global user.email "bruno.resende@gmx.com "

```
# Comandos Básicos Bash
## Criando arquivos

```bash
touch <arquivo.txt> <arquivo2.txt>
```

## Criando pastas
```bash
mkdir <nome_pasta>
```


# Comandos Básicos GIT
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

# Integração com o GitHub

## Criando Repositório do zero
> Seguir instruções do GitHub 

## Clonando repositório 
> Abre o Bash na pasta SUPERIOR a pasta desejada de clonar
```bash
git clone <link_git_hub>
```
## Fazendo Push 
```shell
git push
```




