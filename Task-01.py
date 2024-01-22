#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import os


# In[2]:


os.getcwd()


# In[5]:


os.chdir('C:\\Users\\Abhi\\documents\\readings')


# In[6]:


df=pd.read_csv('World Bank.csv')


# In[7]:


df.head()


# In[8]:


df.info()


# In[37]:


df.columns


# In[9]:


df.dtypes


# In[13]:


df.duplicated().sum()


# In[14]:


df=df.fillna(method="ffill")
df.head()


# In[15]:


df.isna().sum().any()


# In[16]:


top_ten_countries=df.nlargest(n=10,columns=['2022'])
top_ten_countries


# In[38]:


df['Country Name'].unique()


# In[40]:


df['Country Code'].unique()


# In[18]:


#FILTER DATA FOR TOTAL MALE POPUALTION
total_population_male=df[df['Indicator Code']=='SP.POP.TOTAL.MA.IN']
total_population_male


# In[19]:


#SORT DATA BASED ON TOTAL POPULATION FOR 2022
total_population_sort_ma=total_population_male.sort_values(by='2022',ascending=False)
total_population_sort_ma


# In[20]:


#GET TOP 10 COUNTRIES WITH THE HIGHEST POPULATION FOR 2022
top_ten_male_countries=total_population_sort_ma.head(10)
print("Top ten male countries of total population :-")
print(top_ten_male_countries)


# In[22]:


country_by_1960=df.sort_values(by='1960').head(10)
country_by_1960


# In[25]:


gender =['Male','Female','Non-Binary','Other']
count =[80,140,40,25] #Replace with your actual data

#CREATE A BAR CHART
plt.bar(gender,count,color=['Red','Yellow','Green','Orange'])

#ADD LABEL AND TITLE 
plt.xlabel('gender')
plt.ylabel('count')
plt.title('Distribution of gender in a population')
plt.show()


# In[29]:


ages =np.random.normal(loc=30,scale=5,size=900) #Replace with your actual data

#CREATE A HISOTGRAM
plt.hist(ages,bins=30,color='red',edgecolor='black')

#ADD LABELS AND TITLE
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in a population')
plt.show()


# # Thank you

# In[ ]:




