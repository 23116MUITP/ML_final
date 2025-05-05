
import pandas as pd
import re

def extract_hashtags(text):
    return re.findall(r"#(\w+)", text)

def load_data(file):
    df = pd.read_csv(file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hashtags'] = df['post'].apply(extract_hashtags)
    return df
