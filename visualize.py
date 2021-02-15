import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mentions.csv')

print(df)

sns.set_theme(style='whitegrid')
ax = sns.violinplot(x=df['Page Number'], y=df['Book'], hue=df['Query'], inner=None, color='.8')
ax = sns.stripplot(x=df['Page Number'], y=df['Book'], hue=df['Query'], jitter=0.08, linewidth=1)
ax.set_xlabel('Page Number', fontsize=10)
ax.set_ylabel('Book', fontsize=6)
plt.show()
