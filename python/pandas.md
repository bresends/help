# Comandos úteis

```python
# Conta quantos itens de cada tipo tem dentro de uma série
df['coluna_desejada'].value_counts()
```

```python
# Diz quantas linhas e colunas tem um DF
df.shape 
```

```python
# Diz qual o tipo 
df.info() # DF
df.dtypes # Série
```

```python
# Mostra o nomes das colunas de um datafram
df.columns
```

```python
#Faz média e mediana dos valores 
df.describe() 
```

```python

#Joga fora as linhas NaN (que não tem valores)
df.dropna() 
```

```python
# Faz a soma de quantos valores nulos (NaN) tem dentro do DataFrame
df['coluna_desejada'].isnull().sum()
```

```python
# Filtra os valores nulos (NaN) do DF
df[df['coluna_desejada'].isnull()]
```

```python

# Resetando o index pra números
df = df.reset_index()
```

```python
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

## Mudando o nome do index(primeira coluna)

```python
df.index.name == 'Nome'
```
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

# Duplicatas

## Visualisando 

### Linhas iguais repetidas

```python
df.duplicate().sum()
```

### Coluna repetida

```python
df['Coluna'].duplicated().sum()
```

### Mostrando quais são os itens repetidos
```python
# Filtrando valores
df.loc[df['Coluna'].duplicated(keep='first'), :] 
```

## Deletando

```python
df.drop_duplicates(keep='first')
data.drop_duplicates(subset = "First Name", keep = False, inplace = True)
```

# Aplicando Funções

## Séries
```python
def update_value(value):
  return value + 1 

df['user_id'] = df['user_id'].apply(update_value)
```

## DF completo

```python
# Transforma todos os dados em string
df = df.applymap(str)
```

# Unindo DataFrames

## Apenas colando um no fundo do outro

```python
df = pd.concat([df1, df2])
df = df.reset_index(drop=True) # Reseta os Indexes pra juntar tudo começando do zero
```

## Merge

```python

df_resultado = pd.merge(df_1, df_2, how='inner')
df_resultado = pd.merge(df_1, df_2, how='outer')

# Se eu quiser unir apenas por 1 das colunas 
df_resultado = pd.merge(df_1, df_2, on=['Coluna_de_União','Coluna_de_União_2'])

# Se o nome das colunas não bater, posso fazer na mão 
df_resultado = pd.merge(df_1, df_2, left_on=['nome_respectivo_df1'], right_on=['nome_respectivo_df2'])

# Se quiser fazer o merge pelos indexes
df_resultado = pd.merge(df_1, df_2, left_index=True, right_index=True)

# Se quiser por nome nos indicadores de colunas

df_resultado = pd.merge(df_1, df_2, on=['Whatever'], suffixes=('_left', '_right')) 
df_merged = pd.merge(df_tb, df_guru, how='outer', on = 'Ticker', indicator=True, suffixes=('_TB', '_Guru'))
```

# Comparando Dataframes

## Encontrando Itens em Comum nas Duas (Estão em 1 e no outro)

```python
df = pd.merge(df1, df2, how='inner', indicator=False)
```
## Encontrando LINHAS exclusivas de um (Linhas de df1 que não estão em df2)
```python
df = pd.merge(df1, df2, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
```

## Descartando a intersecção (jogando fora todos o itens repetidos em ambos)

```python
pd.concat([df1,df2]).drop_duplicates(keep=False)
```

## Encontrando todos os valores em uma coluna de DFs que não são comuns em ambos

```python
set(df1['Temp']).symmetric_difference(df2['Temp'])
```
