import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    # Load the data
    df = pd.read_csv('medical_examination.csv')
    
    # Calculate BMI
    df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
    df['overweight'] = (df['BMI'] > 25).astype(int)
    
    # Normalize cholesterol and gluc values
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    # Create DataFrame for cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    
    # Draw the catplot
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='bar', height=5, aspect=1.5)
    
    # Save the figure
    fig.savefig('catplot.png')

def draw_heat_map():
    # Load the data
    df = pd.read_csv('medical_examination.csv')
    
    # Calculate BMI
    df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
    df['overweight'] = (df['BMI'] > 25).astype(int)
    
    # Normalize cholesterol and gluc values
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Calculate correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = pd.np.triu(pd.np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', vmin=-1, vmax=1)
    
    # Save the figure
    plt.savefig('heatmap.png')

# Uncomment the lines below for testing and debugging
# draw_cat_plot()
# draw_heat_map()
