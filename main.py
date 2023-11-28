"""
This program uses geopandas to simulate the realtime location of a target by using Pandas. Whenever someone asks "WHERE IS HE???" you can now run this program and find out.
"""

import pandas as pd
import geopandas as gpd
import numpy as np

# Load the shapefile of the geographical area
url = "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_nation_20m.zip"
us = gpd.read_file(url).explode()

# Filter out parts of the U.S. that are far away from the mainland
us = us.loc[us.geometry.apply(lambda x: x.exterior.bounds[2])<-60]

# Get the bounding box of the U.S.
x_min, y_min, x_max, y_max = us.geometry.unary_union.bounds

# Generate random x and y coordinates within the bounding box
np.random.seed(2) # Set seed for reproducible results
N = 10000
rndn_sample = pd.DataFrame({'x':np.random.uniform(x_min,x_max,N),'y':np.random.uniform(y_min,y_max,N)})

# Convert the random x and y coordinates into a GeoDataFrame
rndn_sample = gpd.GeoDataFrame(rndn_sample, geometry = gpd.points_from_xy(x=rndn_sample.x, y=rndn_sample.y), crs = us.crs)

# Filter the random points to only include those that fall within the U.S.
inUS = rndn_sample['geometry'].apply(lambda s: s.within(us.geometry.unary_union))
rndn_sample = rndn_sample.loc[inUS,:]

# Plot the random points for visual inspection of the results
rndn_sample.plot()