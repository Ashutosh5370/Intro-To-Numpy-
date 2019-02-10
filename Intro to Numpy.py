
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a  = np.zeros(3)


# In[3]:


a


# In[5]:


type(a[0])


# In[6]:


a.shape


# In[7]:


x = np.zeros(10)


# In[8]:


x


# In[10]:


x.shape = (10 ,1)


# In[11]:


x


# In[12]:


z = np.ones(10)


# In[13]:


z


# In[14]:


z = np.linspace(2,10,5)


# In[15]:


z


# In[18]:


lst = [1,2,3,4]
s = np.arrat([lst])


# In[19]:


s= np.array([lst])


# In[20]:


s


# In[21]:


type(s)


# In[22]:


s.shape


# In[25]:


z1 = np.random.randint(10 ,size=4)


# In[26]:


z1


# In[27]:


z1[0:3]


# In[28]:


z1[-1]


# In[29]:


import skimage import io 


# In[30]:


get_ipython().system('pip install scikit-image')


# In[31]:


import skimage import io


# In[32]:


python -m pip install --upgrade pip


# In[33]:


python -m !pip install --upgrade !pip


# In[35]:


from skimage import io
photo = io.imread('C:/Users/Ashutosh/Desktop/ch.jpg')
type(photo)


# In[36]:


photo.shape


# In[37]:


import matplotlib.pyplot as plt


# In[38]:


plt.imshow(photo)


# In[39]:


plt.imshow(photo[::-1])


# In[40]:


plt.imshow(photo[100:150 , 200:300])


# In[41]:


photo_sin = np.sin(photo)


# In[42]:


photo_sin


# In[43]:


print(np.sum(photo))


# In[44]:


print(np.argmin(photo))


# In[45]:


z<3


# In[46]:


z[z>3]


# In[47]:


ph = np.where(photo>100 ,255,0)


# In[49]:


plt.imshow(ph)


# In[50]:


a= np.array([1,2,3])
b = np.array([1,2,3])   


# In[51]:


a+b


# In[52]:


a @ b


# In[53]:


np.sort(a)

