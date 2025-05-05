
import altair as alt
import pandas as pd

def plot_trend_chart(df, interactive=False):
    chart = alt.Chart(df).mark_line().encode(
        x='timestamp:T',
        y='count:Q',
        color='hashtags:N'
    ).properties(width=700, height=400)
    return chart.interactive() if interactive else chart

def plot_top_topics(df):
    all_tags = df.explode('hashtags')
    top_tags = all_tags['hashtags'].value_counts().nlargest(10).reset_index()
    top_tags.columns = ['hashtags', 'count']
    return alt.Chart(top_tags).mark_bar().encode(
        x='count:Q',
        y=alt.Y('hashtags:N', sort='-x')
    ).properties(width=700)
