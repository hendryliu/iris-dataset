
# coding: utf-8

# In[23]:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
get_ipython().magic('matplotlib inline')
sns.set(style="white", color_codes=True)
os.chdir("/Users/weimi/Python/iris-dataset")
os.getcwd()


# In[34]:

iris = pd.read_csv("./Iris.csv")
type(iris)
# iris = sns.load_dataset("iris")


# In[4]:

iris.info()


# In[8]:

iris.columns.values


# In[10]:

iris.head()


# In[13]:

iris.describe()


# In[15]:

iris.describe(include=['O'])


# In[17]:

iris["Species"].value_counts()


# In[18]:

dir(iris)


# In[26]:

iris.plot(kind="scatter",x="SepalLengthCm",y="SepalWidthCm")


# In[25]:

sns.plt.show()


# In[33]:

sns.lmplot(x="SepalLengthCm",y="SepalWidthCm",data=iris,fit_reg=False,hue="Species")


# In[28]:

help(sns.lmplot)


# In[ ]:


#%%


