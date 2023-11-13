import plotly.express as px
import pandas as pd

if __name__ == '__main__':

    d = {'Australia': [3],
         'Brazil': [2],
         'Canada': [6],
         'Chile': [3],
         'Denmark': [1],
         'France': [16],
         'Germany': [3],
         'Israel': [1],
         "United States": [5],
         "United Kingdom": [1],
        }

    data = pd.DataFrame(d).T.reset_index()
    data.columns = ['country', 'count']


    database = px.data.gapminder().query('year == 2007')

    df = pd.merge(database, data, how='inner', on='country')
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    )

    fig = px.choropleth(df,
                        locations="country",  # "iso_alpha",
                        locationmode="country names",  # "ISO-3",
                        geojson=f"{url}/world-countries.json",
                        color="count"
                        )

    fig.show()

"""
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':



    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # lat_ts is the latitude of true scale.
    # resolution = 'c' means use crude resolution coastlines.
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, \
                llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='coral', lake_color='aqua')
    # draw parallels and meridians.
    m.drawparallels(np.arange(-90., 91., 30.))
    m.drawmeridians(np.arange(-180., 181., 60.))
    m.drawmapboundary(fill_color='aqua')
    plt.title("Mercator Projection")
    #plt.show()

    fig = plt.gcf()
    fig.savefig('worldmap.png', dpi=400, bbox_inches='tight')
    
"""
