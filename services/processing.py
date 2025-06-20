import pandas as pd

def prepare_dataset():

    df = pd.read_csv("data/Students Social Media Addiction.csv")

    df['Affects_Academic_Performance'] = (df['Affects_Academic_Performance'].apply(lambda x: 1 if x == "Yes" else 0))
    
    df = pd.get_dummies(df, columns=['Relationship_Status', 'Gender'], drop_first=False)
    
    return df
