#!/usr/bin/env python
# coding: utf-8

# In[94]:


# Library Imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as matplt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

get_ipython().run_line_magic('matplotlib', 'inline')


# In[95]:


# Dataset Loading
dataframe = pd.DataFrame(pd.read_excel("https://github.com/Shreyans1602/Machine_Learning_Linear_Regression/raw/main/Dataset.xlsx", sheet_name = 'Dataset', index_col = 'No'))

# Loaded Successfully
print("Data Loaded Successfully")
print("Real Estate Valuation Data Set has {} data points with {} variables each.".format(*dataframe.shape))


# In[96]:


# Pre-Processing Stage
print("Pre-Processing the Data:\n")

# Check for null values in the dataframe
print("Null entries found?: ",("No\n" if dataframe.isnull().sum().sum() == 0 else "Yes\n"))

# Check for duplicate values in the dataframe
print("Duplicate entries found?: ",("No\n" if dataframe.duplicated().sum() == 0 else "Yes\n"))

# Check if there is any categorical values
print("Check for categorical values:")
print(dataframe.dtypes)

# Rename attributes and describe the dataframe
dataframe.rename(
    columns = {
        "X1 transaction date": "Transaction_Date", 
        "X2 house age": "House_Age", 
        "X3 distance to the nearest MRT station": "MRT_Distance",
        "X4 number of convenience stores": "Num_Stores_NearBy",
        "X5 latitude": "Latitude",
        "X6 longitude": "Longitude",
        "Y house price of unit area": "House_Price",
    },
    inplace = True
)

print("\nRenaming the attributes for convenience. The dataframe is as follows:\n")
print(dataframe.head())

print("\nDescription of the dataframe is as follows:")
print(dataframe.describe())

# Printing correlation matrix
print("\nCorrelation matrix is as follows:")
print(dataframe.corr())

# Show the impact of different attributes on the House_Price variable
print("\nMost impactful attributes on House_Price variable are shows below in decending order:")
print(abs(dataframe.corr())['House_Price'].sort_values(ascending = False))


# In[97]:


# Show various plots for visualization of the above information
sns.set(rc = {'figure.figsize':(18,10)})
hmap = sns.heatmap(dataframe.corr(), vmin = -1, vmax = 1)


# In[98]:


# Checking the correlation of all the attributes vs the House_Price variable
sns.barplot(y = dataframe.corr().loc['House_Price'].index, x = dataframe.corr().loc['House_Price'].values)


# In[99]:


# Show plots for effect of each variable on House_Price
columns = dataframe.columns

for i in range(len(columns) - 1):
    matplt.figure(i)
    sns.scatterplot(x = columns[i], y = 'House_Price', data = dataframe)


# In[100]:


for i in range(len(columns) - 1):
    matplt.figure(i)
    sns.barplot(x = columns[i], y = "House_Price", data = dataframe)
    matplt.show()


# In[101]:


# Based on the above heatmap, correlation scatter and bar graphs
# High Correlation Attributes w.r.t target are Distance, Num_Stores_NearBy, Latitude, Longitude, House_Age.
# Neligible Correlation Attributes w.r.t target is No and Transaction_Date.

# Dropping the insignificant attributes from the data set
dataframe = dataframe.drop(['Transaction_Date'], axis = 1)
dataframe.columns


# In[139]:


# Prepare X and Y matrix
X = np.array(dataframe.drop(['House_Price'],axis = 1))
Y = np.array(dataframe['House_Price'])


# In[140]:


# Split train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 99)
X_train.shape, X_test.shape, Y_train.shape, Y_test.shape


# In[141]:


# Model Training Stage
lrsgd = LinearRegression()
lrsgd.fit(X_train, Y_train)


# In[142]:


# Evaluate Performance
mse = mean_squared_error(Y_test,lrsgd.predict(X_test))
print(mse)
r2 = r2_score(Y_test,lrsgd.predict(X_test))
print(r2)


# In[ ]:




