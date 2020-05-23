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
# Importando CSV de uma url (dando nome do header)

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
df = pd.read_csv('http://bit.ly/movieusers', sep='|', header=None, names = user_cols)

# Importando CSV de um localização do Google Drive
df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/us_companies.csv')

# Se quiser abrir determinando quais são os index
pd.read_csv('processed.csv', index_col='o_index_desejado')
```

# Header

```python
#Mudando nomes específicos
df.rename(columns={'occupation': 'profissão', 'age': 'idade'}, inplace=True) #ou põe o inplace ou joga isso em uma variável

#Ex: Fazendo tudo ficar Uppercase
df.columns = [x.lower() for x in df.columns]

```
