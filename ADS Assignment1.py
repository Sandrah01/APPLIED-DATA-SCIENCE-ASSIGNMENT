# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:45:46 2022

@author: udehs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')
# drop the null values
data_BM = data_BM.dropna(how="any")
print(data_BM )

price_by_item = data_BM.groupby('Item_Type').Item_MRP.mean()[:5]
print(price_by_item)



# mean price based on item type
price_by_item = data_BM.groupby('Item_Type').Item_MRP.mean()[:10]
x = price_by_item.index.tolist()
y = price_by_item.values.tolist()
# set figure size
plt.figure(figsize=(14, 8))
# set title
plt.title('Mean price for each item type')
# set axis labels
plt.xlabel('Item Type')
plt.ylabel('Mean Price')
# set xticks 
plt.xticks(labels=x, ticks=np.arange(len(x)))
plt.plot(x, y)
#we created a line chart to denote the mean price per item. The mean price varied according to item type.


def bar_chart(x_axis, list,title):
    plt.figure(figsize=(14,8))
    plt.bar(x_axis,list)
    plt.title(title, fontsize= 8)
    plt.show()
# sales by outlet size
sales_by_outlet_size = data_BM.groupby('Outlet_Size').Item_Outlet_Sales.mean()
# sort by sales
sales_by_outlet_size.sort_values(inplace=True)
x = sales_by_outlet_size.index.tolist()
y = sales_by_outlet_size.values.tolist()
# set axis labels
plt.xlabel('Outlet Size')
plt.ylabel('Sales')
# set title
plt.title('Mean sales for each outlet type')
# set xticks 
plt.xticks(labels=x, ticks=np.arange(len(x)))
plt.bar(x, y, color=['red', 'orange', 'magenta'])
#A bar chart is another simple type of visualization that is used for categorical variables.
#suppose we want to have a look at what is the mean sales for each outlet type. we deduce from this plot that small outlet size has the highest mean sale.


data = data_BM[['Item_Weight', 'Item_MRP']]
# create outlier point shape
red_diamond = dict(markerfacecolor='r', marker='D')
# generate subplots
fig, ax = plt.subplots()
# make the boxplot
plt.boxplot(data.values, labels=['Item Weight', 'Item MRP (price)'], flierprops=red_diamond);