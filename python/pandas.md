# Comandos úteis

```python
# Conta quantos itens de cada tipo tem dentro de uma série
df['coluna_desejada'].value_counts()

# Diz quantas linhas e colunas tem um DF
df.shape 

# Diz qual o tipo 
df.info() # DF
df.dtypes # Série

# Mostra o nomes das colunas de um datafram
df.columns

#Faz média e mediana dos valores 
df.describe() 

#Joga fora as linhas NaN (que não tem valores)
df.dropna() 

# Faz a soma de quantos valores nulos (NaN) tem dentro do DataFrame
df['coluna_desejada'].isnull().sum()

# Filtra os valores nulos (NaN) do DF
df[df['coluna_desejada'].isnull()]

# Resetando o index pra números
df = df.reset_index()

# Verificando se os itens de uma série aumentam ou diminiuem estritamente 
df_list['Net Income'].is_monotonic_decreasing 
df_list['Net Income'].is_monotonic_increasing
```
# Importando um dataframe 

```python
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
df = pd.read_csv('http://bit.ly/movieusers', sep='|', header=None, names = user_cols)
```

# Exportando um dataframe

```python
df.to_csv('/content/drive/My Drive/Colab Notebooks/us_companies.csv', index=False)
```

# Alterando o Header

## Passando Coluna com todos os nomes

```python
#Trocando apenas alguns
df = df.rename(columns = {"a":"c", "b": "d"})
```

## Mudando nomes específicos

```python
df.rename(columns={'occupation': 'profissão', 'age': 'idade'}, inplace=True)
```

## Aplicando funções no Header

```python
df.columns = df.columns.str.replace('I', 'Txengas')
# Vai trocar todos os Is por Txngas no Header
```

```python
#Ex: Fazendo tudo ficar Uppercase
df.columns = [x.lower() for x in df.columns]

```

# Deletando 

## Colunas

```python
df = df.drop(['Sexocupation','Soma'], axis=1)
```

## Linhas

```python
df = df.drop(2, axis=0)
df = df.drop([0,1], axis = 0)
```

# Sorting

```python
df['age'].sort_values(by=['Coluna'], inplace=True, ascending=True)
```

# Filtrando Itens

## Forma Simples
```python
# Simples condição
df[df['Ticker'] == 'Qualquer Coisa']

# Multiplas condições
df[ (df['Coluna_1'] == False) & (df['Coluna_2'] > 2) ]

# Filtrando  os NaN
filtered_df = df[df['var2'].isnull()]
```

## Forma Elaborada

```python
filtro = (df['MS'] == False) & (df['MBI'] == False) & (df['MB']) & (df['CNN'] == False)

df = df_merged.loc[filtro]

# Contra-Filtro 
df.loc[~filtro] # Vai me dar o DF de todas as mulheres que não são estudantes
```
