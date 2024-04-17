#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


# Define the file paths
file_paths = [
    r"C:\Users\melis\Downloads\archive (1)\PRSA_Data_Huairou_20130301-20170228.csv",
    r"C:\Users\melis\Downloads\archive (1)\PRSA_Data_Nongzhanguan_20130301-20170228.csv",
    r"C:\Users\melis\Downloads\archive (1)\PRSA_Data_Tiantan_20130301-20170228.csv",
    r"C:\Users\melis\Downloads\archive (1)\PRSA_Data_Changping_20130301-20170228.csv"
]


# In[4]:


# Initialize an empty DataFrame
combined_df = pd.DataFrame()


# In[5]:


# Read and concatenate the data from each file
for file_path in file_paths:
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)


# In[6]:


# Now combined_df contains the merged data from all four stations
print(combined_df.head())  # Display the first few rows


# In[7]:


last_5_rows = combined_df.tail(5)
print(last_5_rows)


# In[8]:


# Define the AQI breakpoints and corresponding index values for each pollutant
aqi_breakpoints = {
    'PM2.5': [(0, 12), (12.1, 35.4), (35.5, 55.4), (55.5, 150.4), (150.5, 250.4), (250.5, float('inf'))],
    'PM10': [(0, 54), (55, 154), (155, 254), (255, 354), (355, 424), (425, float('inf'))],
    'SO2': [(0, 35), (36, 75), (76, 185), (186, 304), (305, 604), (605, float('inf'))],
    'NO2': [(0, 53), (54, 100), (101, 360), (361, 649), (650, 1249), (1250, float('inf'))],
    'CO': [(0, 4.4), (4.5, 9.4), (9.5, 12.4), (12.5, 15.4), (15.5, 30.4), (30.5, float('inf'))],
    'O3': [(0, 54), (55, 70), (71, 85), (86, 105), (106, 200), (201, float('inf'))]
}


# In[14]:


# Calculate AQI for each pollutant
def calculate_aqi(pollutant, concentration):
    breakpoints = aqi_breakpoints[pollutant]
    for i in range(len(breakpoints)):
        low, high = breakpoints[i]
        if low <= concentration <= high:
            aqi_low, aqi_high = i * 50, (i + 1) * 50
            return ((aqi_high - aqi_low) / (high - low)) * (concentration - low) + aqi_low

# Calculate AQI for each pollutant
for pollutant in aqi_breakpoints:
    combined_df[f'AQI_{pollutant}'] = combined_df[pollutant].apply(lambda x: calculate_aqi(pollutant, x))

# Calculate overall AQI
combined_df['Overall_AQI'] = combined_df[[f'AQI_{pollutant}' for pollutant in aqi_breakpoints]].max(axis=1)

# Now combined_df contains AQI values for all pollutants and overall AQI
print(combined_df[['PM2.5', 'AQI_PM2.5', 'PM10', 'AQI_PM10', 'SO2', 'AQI_SO2', 'NO2', 'AQI_NO2', 'CO', 'AQI_CO', 'O3', 'AQI_O3', 'Overall_AQI']].head())


# In[15]:


combined_df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




