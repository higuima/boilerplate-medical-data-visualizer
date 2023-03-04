import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display

# Import data
df = pd.read_csv('freeCodeCamp/boilerplate-medical-data-visualizer/medical_examination.csv')

# Add 'overweight' column
df['overweight'] = 0
df.loc[df['weight']/((df['height']/100)**2) > 25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(data=df_cat.value_counts(), columns=["total"]).sort_index().reset_index()

    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x="variable", y="total", col="cardio", hue="value", kind="bar").fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))  & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    # Draw the heatmap with 'sns.heatmap()'
    fig, ax = plt.subplots(figsize=(12, 9))
    ax = sns.heatmap(corr,mask=mask,vmax=0.4,square=True,fmt=".1f",annot=True)




    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
