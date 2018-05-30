
# coding: utf-8

# In[93]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/Tran/Downloads/Capstone project 1/Source data/train.csv')


# In[94]:


df_interger = df.select_dtypes(include=['int64'])


# In[109]:


full_list = ['MSSubClass' , 'LotArea' , 'OverallQual' , 'OverallCond' , 'YearBuilt' , 'YearRemodAdd' , 'BsmtFinSF1' ,
           'BsmtFinSF2' , 'BsmtUnfSF' , 'TotalBsmtSF' , '1stFlrSF' , '2ndFlrSF' ,'LowQualFinSF', 'GrLivArea','BsmtFullBath',
           'BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','Fireplaces','GarageCars',
           'GarageArea','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold',
           'YrSold', 'SalePrice']
features_list =['MSSubClass' , 'LotArea' ,'OverallQual' , 'OverallCond' , 'YearBuilt' ]
for i in full_list:
    plt.hist(df[i])
    plt.xlabel(i)
    plt.show()
    

