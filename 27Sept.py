# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Working with Zip

# %%
list1= [1,2,3,4]
list2= ['rajat','malvika','pooja','chandola','rashika']


# %%
for items in zip(list1,list2):
    print(items)

# %% [markdown]
# ## Working with Numpy 
# First Lets install it

# %%
get_ipython().system('pip install numpy')


# %%
import numpy as np
itmes = np.array([23,44,66])
itmes


# %%
cost = np.array([33.4,44.23,12.3])
cost

# %% [markdown]
# # How numpy is faster than List
# 
# Running a loop for list calculation is much slower than running the same fucntionality on numpy 
# ### Numpy is more than 100 times faster than list
# 

# %%
list1 = list(range(1000000))
list2 = list(range(1000000,2000000))

num_list1 = np.array(list1)
num_list2 = np.array(list2)


# %%
get_ipython().run_cell_magic('time', '', 'result = 0\nfor i,j in zip(list1,list2):\n    result +=i*j\nresult')


# %%
get_ipython().run_cell_magic('time', '', 'np.dot(num_list1,num_list2)')


