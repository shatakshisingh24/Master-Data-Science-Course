#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install matplotlib


# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


#Line Plot
x=np.arange(10)
y1= x**2
y2=2*x+34

print(x)
print(y1)
print(y2)


# In[6]:


plt.plot(x,y1)
plt.show


# In[9]:


#Matplotlib provides some themes for plots to get a list of theme write the foloowng code:

themes=plt.style.available
print(themes)


# In[26]:


#Lets use one of these themes 'Seaborn'. You can see the grids in background. Smilarly you can try other themes to get more attractve plots.

plt.style.use("seaborn-paper")
plt.plot(x,y1)
plt.show


# In[28]:


#Let's see how can we change the color of line.

plt.style.use("seaborn-paper")
plt.plot(x,y1, color="red")
plt.plot(x,y2, color="green")

plt.show


# In[30]:


#Let's see how can put lables

plt.style.use("seaborn-paper")
plt.plot(x,y1, color="red")
plt.plot(x,y2, color="green")


plt.xlabel("Tme")
plt.ylabel("Speed")
plt.title("Speed v/s Time Curve")

plt.show


# In[32]:


#Let's see how can we give labels to curves.

plt.style.use("seaborn-paper")
plt.plot(x,y1, color="red", label="A")
plt.plot(x,y2, color="green", label="B")
plt.legend()

plt.xlabel("Tme")
plt.ylabel("Speed")
plt.title("Speed v/s Time Curve")

plt.show


# In[33]:


get_ipython().run_line_magic('pinfo', 'plt.plot')


# In[34]:


#Let's see how can we can change style of a line

plt.style.use("seaborn-paper")
plt.plot(x,y1, color="red", label="A", linestyle="dashed")
plt.plot(x,y2, color="green", label="B")
plt.legend()

plt.xlabel("Tme")
plt.ylabel("Speed")
plt.title("Speed v/s Time Curve")

plt.show


# In[41]:


#Let's see how can we can change style of a line

plt.style.use("seaborn-paper")
plt.plot(x,y1, color="red", label="A", linestyle="dashed", marker="o")
plt.plot(x,y2, color="green", label="B")
plt.legend()

plt.xlabel("Tme")
plt.ylabel("Speed")
plt.title("Speed v/s Time Curve")

plt.show


# In[ ]:




