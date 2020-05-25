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

#Mostrando branch onde estamos trabalhando
```bash
git branch
```

## Retornando a uma versão anterior
```bash
git checkout <codigo_commit>
```

## Voltando tudo pro último commit
```bash
git checkout master
```
