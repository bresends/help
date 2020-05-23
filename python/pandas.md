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

## De uma URL
```python
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
df = pd.read_csv('http://bit.ly/movieusers', sep='|', header=None, names = user_cols)
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
#Ex: Fazendo tudo ficar Uppercase
df.columns = [x.lower() for x in df.columns]

```
