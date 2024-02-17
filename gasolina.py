import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('./gasolina.csv')

with sns.axes_style('whitegrid'):
  plt.figure(figsize=(10, 6))
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', linewidth=5)
  grafico.set_title('Preço da gasolina nos 10 primeiros dias de julho de 2021', fontsize=16)
  grafico.set(xlabel='Dia', ylabel='Preço (R$)')
