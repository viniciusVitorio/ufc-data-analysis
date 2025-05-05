import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

cores = sns.color_palette("Set2")

df = pd.read_csv("data/ufc-master.csv")
df = df.dropna(subset=['Date'])  

df['Year'] = pd.to_datetime(df['Date'], errors='coerce').dt.year

traducao_pesos = {
    'Heavyweight': 'Peso Pesado',
    'Light Heavyweight': 'Meio-Pesado',
    'Middleweight': 'Peso Médio',
    'Welterweight': 'Meio-Médio',
    'Lightweight': 'Peso Leve',
    'Featherweight': 'Peso Pena',
    'Bantamweight': 'Peso Galo',
    'Flyweight': 'Peso Mosca',
    'Women\'s Strawweight': 'Peso Palha (F)',
    'Women\'s Flyweight': 'Peso Mosca (F)',
    'Women\'s Bantamweight': 'Peso Galo (F)',
    'Women\'s Featherweight': 'Peso Pena (F)',
}
df['WeightClassPt'] = df['WeightClass'].map(traducao_pesos).fillna(df['WeightClass'])

ko_tko_count = df[df['Finish'] == 'KO/TKO'].shape[0]
submission_count = df[df['Finish'] == 'SUB'].shape[0]

print(f"Total de Nocautes (KO/TKO): {ko_tko_count}")
print(f"Total de Finalizações (Submission): {submission_count}")

method_counts = df['Finish'].value_counts()
print("\nDistribuição dos Métodos de Vitória:")
print(method_counts)

plt.figure(figsize=(10, 6))
method_counts.plot(kind='bar', color=cores)
plt.title('Distribuição dos Métodos de Vitória', fontsize=16)
plt.xlabel('Métodos de Vitória')
plt.ylabel('Número de Lutas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('images/metodos_vitoria.png', dpi=300)
plt.show()

df['RedExpectedValueWin'] = df['RedExpectedValue'] * (df['Winner'] == 'Red')
df['BlueExpectedValueWin'] = df['BlueExpectedValue'] * (df['Winner'] == 'Blue')

avg_red_expected_win = df[df['Winner'] == 'Red']['RedExpectedValue'].mean()
avg_blue_expected_win = df[df['Winner'] == 'Blue']['BlueExpectedValue'].mean()

print(f"\nValor esperado médio para o Red (quando vence): {avg_red_expected_win}")
print(f"Valor esperado médio para o Blue (quando vence): {avg_blue_expected_win}")

weight_class_performance = df.groupby('WeightClassPt')['Finish'].value_counts().unstack(fill_value=0)
print("\nVitórias por Método de Vitória em Cada Categoria de Peso:")
print(weight_class_performance)

# Gráfico: Vitórias por método x categoria de peso
weight_class_performance.plot(kind='bar', figsize=(12, 6), color=cores)
plt.title('Vitórias por Método de Vitória em Cada Categoria de Peso', fontsize=16)
plt.xlabel('Categoria de Peso')
plt.ylabel('Número de Vitórias')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('images/vitorias_por_peso.png', dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(['KO/TKO', 'Submission'], [ko_tko_count, submission_count], color=cores[:2])
plt.title('Comparação entre Nocautes e Finalizações', fontsize=16)
plt.xlabel('Métodos de Vitória')
plt.ylabel('Número de Lutas')
plt.tight_layout()
plt.savefig('images/comparacao_nocautes_finalizacoes.png', dpi=300)
plt.show()

method_by_year = df.groupby(['Year', 'Finish']).size().unstack(fill_value=0)
method_by_year = method_by_year[method_by_year.index.notnull()]

method_by_year.plot(kind='bar', stacked=True, colormap='tab20', figsize=(14, 7))
plt.title('Métodos de Vitória por Ano', fontsize=18)
plt.ylabel('Número de Lutas')
plt.xlabel('Ano')
plt.xticks(rotation=45)
plt.legend(title="Método", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('images/metodos_por_ano.png', dpi=300)
plt.show()

df_ko_sub = df[df['Finish'].isin(['KO/TKO', 'SUB'])]
round_finish_counts = df_ko_sub.groupby(['Finish', 'FinishRound']).size().reset_index(name='Count')

plt.figure(figsize=(10,6))
sns.barplot(data=round_finish_counts, x='FinishRound', y='Count', hue='Finish', palette=cores)
plt.title('Distribuição dos Rounds de KO/TKO e SUB', fontsize=16)
plt.xlabel('Round')
plt.ylabel('Número de Lutas')
plt.legend(title='Método')
plt.tight_layout()
plt.savefig('images/rounds_ko_sub.png', dpi=300)
plt.show()

df_main = df[df['Finish'].isin(['KO/TKO', 'SUB', 'DEC'])]
finish_year_trend = df_main.groupby(['Year', 'Finish']).size().reset_index(name='Count')

plt.figure(figsize=(14, 7))
sns.lineplot(data=finish_year_trend, x='Year', y='Count', hue='Finish', marker='o', palette=cores)
plt.title('Tendência de Tipos de Vitória ao Longo dos Anos', fontsize=18)
plt.xlabel('Ano')
plt.ylabel('Número de Lutas')
plt.legend(title='Método')
plt.tight_layout()
plt.savefig('images/tendencia_metodos_ano.png', dpi=300)
plt.show()
