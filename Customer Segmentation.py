#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib as mt

# visualisation
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff


# In[5]:


data = pd.read_csv('D:\MyPythonClass\Customer Segmentation Project\customers.csv')
data


# In[15]:


data.isnull().sum()


# In[16]:


data=data.dropna()
data.isnull().sum()


# In[17]:


data.duplicated().sum()


# In[18]:


data.info()


# In[19]:


print('Last subscription ', max(data['Subscription Date']))
print('First subscription ', min(data['Subscription Date']))


# In[20]:


#data analysisand visualization


# In[22]:


data.describe(include=object).T


# In[9]:


data['Subscription Date']=pd.to_datetime(data['Subscription Date'])
data['year']=data['Subscription Date'].dt.year
data['month']=data['Subscription Date'].dt.month
data
# ignore warnings
# import warnings
# warnings.filterwarnings('ignore')
# sns.pairplot(data,vars=['City','Company'],hue ='Index');


# In[22]:


small_data=data.head()
sns.pairplot(data,vars=['year','month'],hue ='month');


# In[31]:


# sns.scatterplot(x=small_data['Country'],y=small_data['year'])
small_data.plot(kind='scatter',
        x='year',
        y='Country',
        color='red')


# In[37]:


small_data.plot(kind='bar',
        x='month',
        y='year',
        color='grey')


# In[40]:


small_data.plot(kind='line',
        x='month',
        y='Subscription Date',
        color='grey')
small_data.plot(kind='line',
        x='year',
        y='Subscription Date',
        color='red')


# In[41]:


small_data.plot(kind='hist',
        x='month',
        y='year',
        color='grey')


# In[ ]:




