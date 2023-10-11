#!/usr/bin/env python
# coding: utf-8

#  dataset:-https://www.kaggle.com/datasets/utkarsharya/ecommerce-purchases

# In[ ]:


import pandas as pd


# In[3]:


data=pd.read_csv("Ecommerce Purchases")
data


# **Display top10 Rows of the Dataset**

# In[5]:


data.head(10)


# **Check last 10 Rows Of the Dataset**

# In[6]:


data.tail(10)


# **Check Datatype of each columns**

# In[7]:


data.dtypes


# **Check Null Values in The Dataset**

# In[9]:


data.isnull().sum()


# **How Many Rows and Columns are there in the dataset**

# In[10]:


data.shape


# In[13]:


len(data.columns)


# In[14]:


len(data)


# **Highest and Lowest Purchase Price**

# In[15]:


data.columns


# In[16]:


highest_purchase_price=data['Purchase Price'].max()
highest_purchase_pric


# In[19]:


lowest_purchase_price=data['Purchase Price'].min()
lowest_purchase_price


# **Averrage purchase Price**

# In[21]:


avg_purchase_price=data['Purchase Price'].mean()


# **How many People Have French 'fr' as their Language**

# In[22]:


data.columns


# In[32]:


len(data[data['Language']=='fr'])


# In[33]:


data[data['Language']=='fr'].count()


# **Job Title Which contains Engineer**

# In[38]:


len(data[data['Job'].str.contains('engineer',case=False)])


# **Find the email of the person with the following IP Addresses 132.207.160.22**

# In[40]:


data[data['IP Address']=='132.207.160.22']['Email']


# **How Many People Have Mastercard As Their Credir card Provider And Made A Purchase above 50**

# In[49]:


len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)])


# **Find the Email of the person with the following credit card no-46648252258997302**

# In[56]:


data[data['Credit Card']==4664825258997302]['Email']


# **How Many People Purchase During the AM and How Many People Purchase During PM**

# In[58]:


data.columns


# In[62]:


data['AM or PM'].value_counts()


# **How Many People have a Credit Card that Expire in 2020**

# In[63]:


data.columns


# In[69]:


def func():
    count=0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count+=1
    print(count)


# In[70]:


func()


# In[74]:


data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')].count()


# **Top 5 Most Popular Email providers (e.g email.com,yahoo.com)**

# In[75]:


list1=[]
for email in data['Email']:
     list1.append(email.split('@')[1])


# In[76]:


data['temp']=list1


# In[80]:


data['temp'].value_counts().head(5)


# In[ ]:




