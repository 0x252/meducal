import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# Add an overweight column to the data. 
#To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms 
#by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

df['overweight'] = (((df['weight'] / 10000) / (df['height'] / 1000)**2 * 100 > 25)).astype(np.int8)

# 3
df.loc[df['cholesterol'] == 1,'cholesterol'] = 0
df.loc[df['cholesterol'] > 1,'cholesterol'] = 1
df.loc[df['gluc'] == 1,'gluc'] = 0
df.loc[df['gluc'] > 1,'gluc'] = 1
# 4
def draw_cat_plot():
    # 5
    global df
    # DataFrame.melt(id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])

    #print(df_cat)
    # 6
    # 
    #df_cat = df_cat.groupby(['cardio', 'variable', 'value'])
    

    # 7
    # https://seaborn.pydata.org/generated/seaborn.catplot.html
    catplot = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count')
    catplot.set_ylabels("total")

    # 8
    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    global df_heat
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13 by chatgpt because I not clear what there need. mask not tested
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(corr, mask=mask, cmap="coolwarm", annot=True, fmt=".1f", square=True, center=0)

    # 16
    fig.savefig('heatmap.png')
    return fig