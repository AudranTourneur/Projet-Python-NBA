import plotly.express as px
import pandas as pd

df = pd.read_json('stats.json')
df.columns = ['PLAYER_ID', 'COUNTRY']

# Change USA to United States
df['COUNTRY'] = df['COUNTRY'].replace('USA', 'United States')

if __name__ == '__main__':

    d = df['COUNTRY'].value_counts().to_dict()
    # Put each datas in [] to be able to use it in the choropleth
    d = {k: [v] for k, v in d.items()}

    data = pd.DataFrame(d).T.reset_index()
    data.columns = ['country', 'count']

    database = px.data.gapminder().query('year == 2007')

    df = pd.merge(database, data, how='inner', on='country')
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    )

    # Ignore United States 
    df_stats = df[df['country'] != 'United States']
    fig = px.choropleth(df_stats,
                        locations="country",  # "iso_alpha",
                        locationmode="country names",  # "ISO-3",
                        geojson=f"{url}/world-countries.json",
                        color="count"
                        )
    
    # Add a title
    fig.update_layout(title_text='Number of players by country')
    
    # Add a text to tell the percentage of players in the top 5 countries
    top1 = df['count'].max()
    top2 = df['count'].sort_values(ascending=False).iloc[1]
    top3 = df['count'].sort_values(ascending=False).iloc[2]
    top4 = df['count'].sort_values(ascending=False).iloc[3]
    top5 = df['count'].sort_values(ascending=False).iloc[4]
    
    top1_country = df[df['count'] == top1]['country'].iloc[0]
    top2_country = df[df['count'] == top2]['country'].iloc[0]
    top3_country = df[df['count'] == top3]['country'].iloc[0]
    top4_country = df[df['count'] == top4]['country'].iloc[0]
    top5_country = df[df['count'] == top5]['country'].iloc[0]
    
    top1_percentage = round(top1 / df['count'].sum() * 100, 2)
    top2_percentage = round(top2 / df['count'].sum() * 100, 2)
    top3_percentage = round(top3 / df['count'].sum() * 100, 2)
    top4_percentage = round(top4 / df['count'].sum() * 100, 2)
    top5_percentage = round(top5 / df['count'].sum() * 100, 2)
    
    fig.add_annotation(x=0.5, y=-0.1,
                          text=f'Top 5 countries: {top1_country} ({top1_percentage}%), {top2_country} ({top2_percentage}%), {top3_country} ({top3_percentage}%), {top4_country} ({top4_percentage}%), {top5_country} ({top5_percentage}%)',
                          showarrow=False,
                          xref="paper",
                          yref="paper",
                          font=dict(
                            size=14,
                            color="black"
                          )
                          )

    fig.show()