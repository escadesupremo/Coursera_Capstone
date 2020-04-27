#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('conda install -c bioconda perl-xml-parser --yes')
get_ipython().system('conda install -c anaconda beautifulsoup4 --yes')
get_ipython().system('conda install -c anaconda lxml --yes')
from bs4 import BeautifulSoup #Needed for web scraping
import requests #Needed for handling requests
import pandas as pd #Using to create dataframes and manipulate data
get_ipython().system('conda install -c conda-forge geopy --yes')
get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium #Geographic visualization
from geopy.geocoders import Nominatim #Handling Coordinates for requesting data through Foursqare API
from pandas.io.json import json_normalize #Normalizing JSON messages for data analysis
import numpy as np


# In the web research phase, the author intends to scrape information from relevant websites in order to determine what would be the ideal location to open a Hungarian fine dining restaurant.

# In[3]:


hungarian_americans = requests.get('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_income').text
hungarian_americans2 = requests.get('https://en.wikipedia.org/wiki/Hungarian_Americans').text
hungarian_americans3 = requests.get('https://simple.wikipedia.org/wiki/List_of_U.S._states%27_largest_cities').text
hungarian_americans4 = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_counties_by_per_capita_income').text
#URLs for web research and analysis                               
soup  = BeautifulSoup(hungarian_americans,'lxml')
soup2 = BeautifulSoup(hungarian_americans2, 'lxml')
soup3 = BeautifulSoup(hungarian_americans3, 'lxml')
soup4 = BeautifulSoup(hungarian_americans4, 'lxml')
#Pairing with BeautifulSoup to scrape tables
tables = soup.find('table', class_ = "wikitable")
tables2 = soup2.find('table', class_ = "wikitable")
tables3 = soup3.find('table', class_ = "wikitable")
tables4 = soup4.find('table', class_ = "wikitable")


# The author found a table containing the size of hungarian-american population in the different states across the US. The author's hypothesis works on the assumption that opening a Hungarian restaurant needs to happen in a major city where hungarian-american and eastern european heritage is significant, as well as has strong economic power.

# In[4]:


row= []
for tr in tables2.find_all('tr'):
    data = tr.find_all('td')
    row.append([i.text.strip() for i in data]) 
labels = tables2.find_all('th')
labels = [c.text for c in labels]
labels = [i.strip() for i in labels] #Scraping table contents from Wikipedia website 
df2 = pd.DataFrame( data  = row , columns = labels) #Putting results into a Pandas Dataframe
new_data = df2.drop([0]) #Dropping the first line of the dataframe
new_data = new_data.rename(columns={'Population[9]':'Population'}) #Renaming one of the columns for better readibility
new_data


# Now there is a list of 7 states with a significant hungarian-american population. The author intends to pair that with the median income for each one of those states. In order to do that, the median income of those states needs to be scraped from the web.

# In[5]:


row= []
for tr in tables.find_all('tr'):
    data = tr.find_all('td')
    row.append([i.text.strip() for i in data]) 
labels = tables.find_all('th')
labels = [c.text for c in labels]
labels = [i.strip() for i in labels] 
df = pd.DataFrame( data  = row , columns = labels)
df= df.drop([0])
df.rename(columns={'State or territory':'State', '2018':'Median Income'}, 
                 inplace=True) #Renaming olumns in order to ease merging with other data.
df.head(1) #Sampling the dataframe


# In order to identify the possible best locations for further analysis, the author identifies the hiearchy of the "hungarian-american states" by adding median income numbers.

# In[6]:


merged_data = pd.merge(new_data, df[["State", "Median Income"]], on="State", how="left")
merged_data = merged_data.sort_values(by=['Median Income'], ascending=False)
merged_data


# At this point, it is assumed that New Jersey, California and New York states are very likely favorable locations for a new Hungarian restaurant overseas.

# In order to narrow the search, it is vitally important to pinpoint some big cities and assess the size of the population. This will help the author determine the size of potential markets. In order to do this, the author will pull and pair the populous of the biggest cities in the "hungarian-american states".

# In[7]:


row= []
for tr in tables3.find_all('tr'):
    data = tr.find_all('td')
    row.append([i.text.strip() for i in data]) 
labels = tables3.find_all('th')
labels = [c.text for c in labels]
labels = [i.strip() for i in labels] 
df3 = pd.DataFrame( data  = row , columns = labels)
df3 = df3.rename(columns={'State,Federal District,or Territory':'State'})
df3 = df3.drop([0])
df3.head(1)


# Pairing this table with the initial one to enhance understanding.

# In[8]:


merged_data2 = pd.merge(merged_data, df3[["State", 'Most populous', "City population"]], on="State", how="left")
merged_data2


# Even though New Jersey has the highest median income out of all states, its biggest city Newark has a population of 277K people. The author intends to point out that based on the fact that Hungarian cuisine is relatively unknown overseas, a small market disqualifies New Jersey as a potential location.

# In order to further enhance understanding, the author decided to pull median income for cities, a further indicator of economic strength and indiciation of spending power.

# In[9]:


row= []
for tr in tables4.find_all('tr'):
    data = tr.find_all('td')
    row.append([i.text.strip() for i in data]) 
labels = tables4.find_all('th')
labels = [c.text for c in labels]
labels = [i.strip() for i in labels] 
df4 = pd.DataFrame( data  = row , columns = labels)
df4 = df4.drop([0])
df4.head(1)


# In order to choose the location, Median Family Income will be used to determine the city to be targeted. Lets see what our top3 potential locations are.

# In[10]:


df4 = df4.rename(columns={'State, federal district or territory':'State'})
values = ["New York County", "Los Angeles", "Philadelphia"]
df4 = df4.loc[df4['County or county-equivalent'].isin(values)]


merged_data3 = pd.merge(merged_data2, df4[["State", 'Medianhouseholdincome']], on="State", how="left")


merged_data3 = merged_data3.rename(columns={'Population': 'Hungarian Ancestry Population','2018':'Median Household Income / State', 'Most populous': 'Biggest City', 'Medianhouseholdincome': 'Median Household Income / City'})
merged_data3 = merged_data3.replace(np.nan, '', regex=True)
merged_data3 = merged_data3.sort_values(by=['Median Household Income / City'], ascending=False)
merged_data3.head(3)


# As shown on the above list, New York has the **biggest population**, **median household income** and **hungarian-american** population, it is decided that **New York** will be targeted to open a new Hungarian restaurant.

# In the second phase of the analysis, the author will be working with some Foursquare data to pinpoint possible locations for the restaurant in NYC.

# In[11]:


CLIENT_ID = 'Y2NPMAP2FXXT22HUQOAKKNDAMUQHUOZ2PN3DOSQVGYCKBYE5' 
CLIENT_SECRET = '54NFIC2OFJ3JAUFAGAEUP1OP3A2AMVHUONV5Q1UWJI0EXTGS' 
VERSION = '20200425'
LIMIT = 1000

address = 'Manhattan, New York, United States'
#User specific information to ask for Foursquare data.

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
#Translating location information to latitutes and longitudes

search_query = 'Hungarian' #Looking for all Hungarian venues in NYC.
radius = 60000 #Within a radius of 60km
url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, search_query, radius, LIMIT)
results = requests.get(url).json


# In[12]:


results = requests.get(url).json() #Request JSON from Foursquare API
venues = results['response']['venues'] #Get venues data from JSON


dataframe = json_normalize(venues)
dataframe.head(3) #Normalize JSON results into a Pandas dataframe and sample data


# In order to better understand this data, we need to extract category types, which is nested inside categories.

# In[13]:


# Stripping down dataset to only include category, name and location related data.
filtered_columns = ['name', 'categories'] + [col for col in dataframe.columns if col.startswith('location.')] + ['id']
dataframe_filtered = dataframe.loc[:, filtered_columns]

#Function to get category, thanks for this Coursera!
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']

#Filtering the categories to ease understanding
dataframe_filtered['categories'] = dataframe_filtered.apply(get_category_type, axis=1)

#Further cleaning column names
dataframe_filtered.columns = [column.split('.')[-1] for column in dataframe_filtered.columns]
dataframe_filtered.head(1)


# The author's intention is to group Hungarian-related venues in NYC according to eatery/non-eatery categories. In order to support this, some cleansing is needed.

# In[14]:


ny_hungarian = dataframe_filtered[['name','categories','lat','lng']]

food_venues = ["Snack Place", "Coffee Shop", 'Bakery', 'Hungarian Restaurant', 'Deli/Bodega','Food', 'Restaurant', 'Eastern European Restaurant']
food_nyc = ny_hungarian.loc[ny_hungarian['categories'].isin(food_venues)]

other_venues = ['Event Space', 'Performing Arts Venue', 'Assisted Living', 'Embassy / Consulate', 'Church', 'Construction & Landscaping', 'Office', 'Grocery Store' 'History Museum', 'Nightlife Spot', 'Grocery Store', 'Building', 'None', 'Soccer Stadium']
other_venues = ny_hungarian.loc[ny_hungarian['categories'].isin(other_venues)]


# In[15]:


food_nyc.shape #We found 9 food and hungarian related venues in NYC and surrounding areas.


# In[16]:


other_venues.shape #We have found 19 venues which are not food but hungarian related in NYC


# Lets see where the direct competition is located for the restaurant and visualize results on a map.

# In[17]:


venues_map = folium.Map(location=[40.77, -73.90], zoom_start=10)

for lat, lng, label in zip(food_nyc['lat'], food_nyc['lng'], food_nyc['name']):
        folium.features.CircleMarker(
            [lat, lng],
            radius=3,
            poup=label,
            fill=True,
            color='red',
            fill_color='red',
            fill_opacity=0.6
        ).add_to(venues_map)
        
geo_json = 'https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON'

venues_map.choropleth(
    geo_data=geo_json,
    fill_color='black', 
    key_on='feature.properties.boro_name.bronx',
    fill_opacity=0.0, 
    line_opacity=1,
)
venues_map


# As it is clearly visible on the map, the majority of the restaurant's competition is in the Manhattan borough, while there is one hungarian eatery in Brooklyn and Queens.

# Lets see how this maps looks like if the other Hungarian venues are added to the map.

# In[18]:


venues_map = folium.Map(location=[40.77, -73.90], zoom_start=10)

for lat, lng, label in zip(food_nyc['lat'], food_nyc['lng'], food_nyc['name']):
        folium.features.CircleMarker(
            [lat, lng],
            radius=3,
            poup=label,
            fill=True,
            color='red',
            fill_color='red',
            fill_opacity=0.6
        ).add_to(venues_map)
        
for lat, lng, label in zip(other_venues['lat'], other_venues['lng'], other_venues['name']):
        folium.features.CircleMarker(
            [lat, lng],
            radius=4,
            poup=label,
            fill=True,
            color='blue',
            fill_color='blue',
            fill_opacity=0.6
        ).add_to(venues_map)
        
geo_json = 'https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON'

venues_map.choropleth(
    geo_data=geo_json,
    fill_color='black', 
    key_on='feature.properties.boro_name.bronx',
    fill_opacity=0.0, 
    line_opacity=1,
)
venues_map


# It is now visible that the majority of Hungarian restaurants and venues are in Manhattan, projecting a strong competition for the potential Restaurant.

# The author intends to explore the neighboring two boroughs, Queens and Brooklyn as a potential location for the restaurant.

# In[19]:


def get_venues(lat,lng):
    
    #Variables Needed for API call
    radius=1000
    LIMIT=100
    CLIENT_ID = 'Y2NPMAP2FXXT22HUQOAKKNDAMUQHUOZ2PN3DOSQVGYCKBYE5'
    CLIENT_SECRET ='54NFIC2OFJ3JAUFAGAEUP1OP3A2AMVHUONV5Q1UWJI0EXTGS' 
    VERSION = '20200425' 
    #Version and Credentials
    
    #URL to call for data
    url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius, 
            LIMIT)
    
    #This is where we call the data.
    results = requests.get(url).json()
    venue_data=results["response"]['groups'][0]['items']
    venue_details=[]
    for row in venue_data:
        try:
            venue_id=row['venue']['id']
            venue_name=row['venue']['name']
            venue_category=row['venue']['categories'][0]['name']
            venue_details.append([venue_id,venue_name,venue_category])
        except KeyError:
            print('this shit aint good')
        
    column_names=['ID','Name','Category']
    df = pd.DataFrame(venue_details,columns=column_names)
    return df


# In[20]:


def get_new_york_data():
    url='https://cocl.us/new_york_dataset'
    resp=requests.get(url).json()
    #This is a dataset provided by Coursera, thanks guys!
    features=resp['features']
    
    #Defining the dataframe to load data to
    column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] 
    #Instantiate dataframe
    new_york_data = pd.DataFrame(columns=column_names)
    
    for data in features:
        borough = data['properties']['borough'] 
        neighborhood_name = data['properties']['name']
        
        neighborhood_latlon = data['geometry']['coordinates']
        neighborhood_lat = neighborhood_latlon[1]
        neighborhood_lon = neighborhood_latlon[0]
    
        new_york_data = new_york_data.append({'Borough': borough,
                                          'Neighborhood': neighborhood_name,
                                          'Latitude': neighborhood_lat,
                                          'Longitude': neighborhood_lon}, ignore_index=True)
    
    return new_york_data


# We need to filter results for only Brooklyn and Queens.

# In[21]:


new_york_data=get_new_york_data()

new_york_boros = ["Queens", "Brooklyn"]
new_york_data = new_york_data.loc[new_york_data['Borough'].isin(new_york_boros)]#Filtering results for Brooklyn and Queens only.
new_york_data.head(2) #Sampling the results


# Now the author extracted all needed location and Neighborhood coordinates, lets pair those with all restaurant type of venues in the different neighborhoods. This will be used to determine a location where there is no large density of restaurants and is still in close proximity to Manhattan.

# In[22]:


# prepare neighborhood list that contains indian restaurant
column_names=['Borough', 'Neighborhood', 'ID','Name']
nyc_restaurants=pd.DataFrame(columns=column_names)
count=1
for row in new_york_data.values.tolist():
    Borough, Neighborhood, Latitude, Longitude=row
    try:
        venues = get_venues(Latitude,Longitude)
        resturants=venues[venues['Category']=='Restaurant'] 
    except: 
        pass 
    for resturant_detail in resturants.values.tolist():
        id, name , category=resturant_detail
        nyc_restaurants = nyc_restaurants.append({'Borough': Borough,
                                                'Neighborhood': Neighborhood, 
                                                'ID': id,
                                                'Name' : name
                                               }, ignore_index=True)
    count+=1


# Lets see how the sample of this data looks like.

# In[23]:


nyc_restaurants.head(2)


# Lets see how many restaurants does Brooklyn and Queens have.

# In[24]:


nyc_restaurants['count'] = nyc_restaurants.groupby('Borough')['Borough'].transform('count')
new = nyc_restaurants[['Borough', 'count']].copy()
new = new.drop_duplicates('Borough')
new


# According to Foursquare, there are a total number of 58 venues labeled as restaurants in Brooklyn and 37 in Queens.

# Lets see how the distribution of those restaurants look like on a map.

# In[25]:


nyc_restaurants['count'] = nyc_restaurants.groupby('Neighborhood')['Neighborhood'].transform('count')
new2 = nyc_restaurants[['Borough', 'Neighborhood', 'count']].copy()
new2 = new2[['Borough', 'Neighborhood', 'count']]
new2.head(2)


# In[26]:


gjson = r'https://raw.githubusercontent.com/veltman/snd3/master/data/nyc-neighborhoods.geo.json'
nyc_map = folium.Map(location=[40.77, -73.90], zoom_start=10)

#Generate NYC Map
nyc_map.choropleth(
    geo_data=gjson,
    data=new2,
    columns=['Neighborhood', 'count'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=1,
    legend_name='Restaurant Count in NYC'
)
nyc_map


# It seems that both in Brooklyn and Queens, the areas in close proximity to Manhattan are not densely populated with restaurants, hence could be ideal to open a new venue there.
