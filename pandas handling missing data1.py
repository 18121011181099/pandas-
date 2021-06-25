#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
df = pd.read_csv('weather_data.csv',parse_dates=['day']) ## prase_dates function is a timestramp
df.set_index('day',inplace=True)
df
## setting index as day


# In[56]:


new_df = df.fillna(0) ## fillna fun is used fill the empty value by any value
new_df


# In[57]:


new_df = df.fillna( { 'temperature':0 , 'windspeed':0 ,'event':'no event'} ) ## CHANGING PERTICULAR COLOUM BY USING FILLNA FUNCTION 
new_df


# In[58]:


NEW_DF=df.fillna(method='ffill') ## FORWARD FILLING OF THE VALUES USING FFILL
NEW_DF


# In[59]:


anyvalue=df.fillna(method='bfill')##  backward fill
anyvalue


# In[60]:


## we can aslo copy data vertically or horizontally byb suing axis fun . wait let me show anurag


# In[61]:


see=df.fillna(method="bfill" , axis='columns') ## see i copy data horizontally
see


# In[62]:


new_df=df.fillna(method="ffill" , limit=2)
new_df


# In[63]:


new_df=df.interpolate()### interpolate function giving better intermidiate points(linear interpolate)
new_df


# In[64]:


new_df=df.interpolate(method='time')## now this data also use time or day to predict the empty value  
new_df


# In[65]:


new_df=df.dropna()## dropna fun use to drop all the empty value 
new_df


# In[66]:


new_df=df.dropna(how='all')## this how=all use to drop the value which is hole empty in horizontal row
new_df


# In[67]:


new_df=df.dropna(thresh=2)## 2 means i need 2 valid value to show in table 
new_df


# In[68]:


dt=pd.date_range('01-01-2017','01-11-2017')## making date from 1 to 10
idx = pd.DatetimeIndex(dt)
df=df.reindex(idx)
df


# In[ ]:





# In[ ]:




