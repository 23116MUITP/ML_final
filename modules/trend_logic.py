
import pandas as pd

def prepare_trend_data(df, time_col, topic_col, freq, selected_topics):
    df = df.explode(topic_col)
    df = df[df[topic_col].isin(selected_topics)]
    df_grouped = df.groupby([pd.Grouper(key=time_col, freq=freq), topic_col]).size()
    return df_grouped.reset_index(name='count')
