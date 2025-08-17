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


    # 8
    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
