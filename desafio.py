import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

from google.colab import files
arq = files.upload()

df = pd.read_excel()

df.head()

df.shape()

df.type()

df.shape()

df['Valor venda'].sun

df['custo'] = df['custo unitário'].mul(df['quantidade'])

round(df['custo'].sun(), 2)

df['lucro'] = df['valor de venda'] - df['custo']

round(df['lucro'].sun(), 2)

df['tempo de envio'] = df['data de envio'] - df['data de venda']

df['tempo de envio'] = df['data de envio'] - df['data de venda'].dt.days

df.groupby('marca')['tempo de envio'].mean

df.groupby(['data de venda']).dt.year, ['marca']).['lucro'].sum()

pd.options.display.float_format = '{:20,.2f}'.fomart

lucro_ano = df.groupby(['data venda'].dt.year, ["marca"])['lucro'].sum().reset_index()lucro_ano

df.groupby('produto')['quantidade'].sum().sort_values(ascending=false)

df.groupby('produto')['quantidade'].sum().sort_values(ascending=true).plot.barh(title="total produtos vendidos")
plt.xlabel('produto')
plt.ylabel('total')

df.groupby(df['data venda'].dt.year['lucro'].sum().plot.bar(title="lucro por ano")
plt.xlabel('ano')
plt.ylabel('receita')

df_2009 = df(df['data venda'].dt.year == 2009)

df_2009.groupby(df_2009['data venda'].dt.month['lucro'].sum().plot.bar(title="lucro por mês")
plt.xlabel('mês')
plt.ylabel('lucro')
plt.xticks(rotation='horizontal');
                
df_2009.groupby('marca')['lucro'].sum().plot.bar(title="lucro por marca")
plt.xlabel('marca')
plt.ylabel('lucro')
plt.xticks(rotation='horizontal');
                
df_2009.groupby('marca')['lucro'].sum().plot.bar(title="lucro por marca")
                
plt.xlabel('marca')
plt.ylabel('lucro')
plt.xticks(rotation='horizontal');
                
df_2009.groupby('classe')['lucro'].sum().plot.bar(title="lucro por marca")
plt.xlabel('classe')
plt.ylabel('lucro')
plt.xticks(rotation='horizontal');
               
df['tempo de envio'].describe()
                
plt.boxplot(df['Tempo de envio']);
                
plt.hist(df['Tempo de envio']);
                
df['tempo de envio'].max()
                
df[df['tempo de envio'] == 20]
               
df.to_csv('', index=false)
