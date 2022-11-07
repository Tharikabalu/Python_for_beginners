#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
df=pd.read_csv('music.csv')
df


# In[17]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
input=df.drop(columns=['genre'])
output=df['genre']
x_train,x_test,y_train,y_test=train_test_split(input,output,test_size=0.2)


# In[18]:


from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)


# In[19]:


predictions=classifier.predict(x_test)


# In[20]:


score=accuracy_score(y_test,predictions)
score


# In[ ]:




