import geopandas as gpd
import geodatasets

# Use the available 'land' dataset from Natural Earth
path = geodatasets.get_path('naturalearth.land')
world = gpd.read_file(path)

# Note: 'naturalearth.land' contains physical boundaries. 
# It does not contain 'pop_est' or 'gdp_md_est'.
# Let's see what columns ARE available:
print("Available columns:", world.columns.tolist())

# Basic visualization to confirm it's working
world.plot()
print(world.head())