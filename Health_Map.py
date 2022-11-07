import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
import pandas as pd
countries_path = r'C:\Users\U-ser\Downloads\Health map - Sheet1.csv'
df  = pd.read_csv(countries_path, sep = r'\s*,\s*', engine = 'python')

df_geo = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.Percentages, df.health))
#get built in dataset from geopandas
world_data = gpd.read_file(gpd.dataset.get_path('naturalearth_lowres'))
#plot world map
axis = world_data[world_data.continent == 'Africa'].plot(color = 'lightblue', edgecolor = 'black')

df_geo.plot(ax = axis, color = 'black')
plt.title('Health')

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(9,6)
fig.savefig('mathplot.png', dpi = 200)
plt.show()

f = px.choropleth(df, locationmode = 'country names', locations = df['countries'], scope = 'africa', color = df['country'])
f.show()