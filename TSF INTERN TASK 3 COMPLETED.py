#!/usr/bin/env python
# coding: utf-8

# # Name- Rahul Mohaniya
#  

# # DATA ANALYSIS ON A US RETAIL FIRM 
# # TSF INTERN TASK 3
#  

# importing the libraries

# In[17]:


import math
import warnings
import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')


# #LOADING THE DATA

# In[8]:


df = pd.read_csv('E:\Global Terrorism - START data\SampleSuperstore.csv')


# In[9]:


df.head()


# In[12]:


print(df.shape)
print(df.columns.tolist())


# # DATA PREPROCESSING
# Let's Check if dataset contain null values

# In[19]:


df.isnull().sum()


# let's check if data contain any duplicate values

# In[21]:


df.duplicated().sum()


# Deleting duplicate data 

# In[22]:


df.drop_duplicates(keep='first', inplace=True)
df.shape


# In[24]:


for column in df.columns.tolist():
    if len(df[column].unique())< 50:
        print(column,' : ' ,df[column].unique().tolist())


# DROP THE COUNTRY COLUMN BECAUSE IT HAS ONLY ONE VALUES

# In[26]:


df.drop(columns ='Country', inplace= True)
df.head()


# # Exploratory data analysis 
# Now, let's visualise the count plot and Bar Plots for Sales and Profit for the columns: Ship Mode, Segment, Region, and Category.

# In[32]:


f, ax = plt.subplots(1, 3, figsize=(20,4))
sns.countplot(df['Ship Mode'], color = 'steelblue', order = df['Ship Mode'].value_counts().index, ax=ax[0])
ax[0].title.set_text("Orders Count of ship mode")
ax[0].set_xlabel("Ship Mode")
ax[0].set_ylabel("Orders")

ship_sale_profit = df.groupby('Ship Mode')[['Sales', 'Profit']].sum()
ship_sale_profit.sort_values(['Sales'], axis = 0, ascending = False, inplace = True) 
ship_sale_profit.plot(y='Sales', kind = "bar", color = 'steelblue', ax=ax[1])

ax[1].title.set_text('Sales in each Ship Mode')
ax[1].set_xlabel('Ship Mode')
ax[1].set_ylabel('Sales')
ax[1].get_legend().remove()

ship_sale_profit.sort_values(['Profit'], axis = 0, ascending = False, inplace = False) 
ship_sale_profit.plot(y='Profit', kind = "bar", color = 'steelblue', ax=ax[2])

ax[2].title.set_text('Profit in each Ship Mode')
ax[2].set_xlabel('Ship Mode')
ax[2].set_ylabel('Profit')
ax[2].get_legend().remove()

f.autofmt_xdate(rotation=0, ha='center')
plt.show()




# We observe that Standard Class is the most popular shipping mode and Same Day is the least popular. Because Standard Class has the most shipments and it is a cheap shipping mode, it makes sense for it to be the most profitable

# In[68]:


f, ax = plt.subplots(1, 3, figsize=(20,4))

sns.countplot(df['Segment'], color = 'limegreen', order = df['Segment'].value_counts().index, ax=ax[0])
ax[0].title.set_text("Order Count of Segment")
ax[0].set_xlabel("Segment")
ax[0].set_ylabel("Orders")


segment_sale_profit = df.groupby('Segment')[['Sales', 'Profit']].sum()

segment_sale_profit.sort_values(['Sales'], axis = 0, ascending = False, inplace = True) 
segment_sale_profit.plot(y='Sales', kind = "bar", color = 'limegreen', ax=ax[1])

ax[1].title.set_text('Sales in each Segment')
ax[1].set_xlabel('Segment')
ax[1].set_ylabel('Sales')
ax[1].get_legend().remove()


segment_sale_profit.sort_values(['Profit'], axis = 0, ascending = False, inplace = True) 
segment_sale_profit.plot(y='Profit', kind = "bar", color = 'limegreen', ax=ax[2])

ax[2].title.set_text('Profit in each Segment')
ax[2].set_xlabel('Segment')
ax[2].set_ylabel('Profit')
ax[2].get_legend().remove()

f.autofmt_xdate(rotation=0, ha='center')
plt.show()
segment_sale_profit.head()


# We observe that Consumer is the major segment, while Home Office contributes the least.

# In[69]:


f, ax = plt.subplots(1, 3, figsize=(20,4))

sns.countplot(df['Region'], color = 'darkorange', order = df['Region'].value_counts().index, ax=ax[0])
ax[0].title.set_text("Order Count of Region")
ax[0].set_xlabel("Region")
ax[0].set_ylabel("Orders")


region_sale_profit = df.groupby('Region')[['Sales', 'Profit']].sum()

region_sale_profit.sort_values(['Sales'], axis = 0, ascending = False, inplace = True) 
region_sale_profit.plot(y='Sales', kind = "bar", color = 'darkorange', ax=ax[1])

ax[1].title.set_text('Sales in each Region')
ax[1].set_xlabel('Region')
ax[1].set_ylabel('Sales')
ax[1].get_legend().remove()


region_sale_profit.sort_values(['Profit'], axis = 0, ascending = False, inplace = True) 
region_sale_profit.plot(y='Profit', kind = "bar", color = 'darkorange', ax=ax[2])

ax[2].title.set_text('Profit in each Region')
ax[2].set_xlabel('Region')
ax[2].set_ylabel('Profit')
ax[2].get_legend().remove()

f.autofmt_xdate(rotation=0, ha='center')
plt.show()
region_sale_profit.head()


# We observe that West consists of most buyers while South consists of the least. Central region is the least profitable.

# In[70]:


f, ax = plt.subplots(1, 3, figsize=(20,4))

sns.countplot(df['Category'], color = 'rebeccapurple', order = df['Category'].value_counts().index, ax=ax[0])
ax[0].title.set_text("Order Count of Category")
ax[0].set_xlabel("Category")
ax[0].set_ylabel("Orders")


category_sale_profit = df.groupby('Category')[['Sales', 'Profit']].sum()

category_sale_profit.sort_values(['Sales'], axis = 0, ascending = False, inplace = True) 
category_sale_profit.plot(y='Sales', kind = "bar", color = 'rebeccapurple', ax=ax[1])

ax[1].title.set_text('Sales in each Category')
ax[1].set_xlabel('Category')
ax[1].set_ylabel('Sales')
ax[1].get_legend().remove()


category_sale_profit.sort_values(['Profit'], axis = 0, ascending = False, inplace = True)
category_sale_profit.plot(y='Profit', kind = "bar", color = 'rebeccapurple', ax=ax[2])

ax[2].title.set_text('Profit in each Category')
ax[2].set_xlabel('Category')
ax[2].set_ylabel('Profit')
ax[2].get_legend().remove()

f.autofmt_xdate(rotation=0, ha='center')
plt.show()
category_sale_profit.head()


# We observe that the frequency of purchases in the Office Supplies category is significantly large as compared to Technology and Furniture. However, the sales amount for Technology is the highest, which makes sense because technological equipments are expensive, thus resulting in a larger sales despite a lower frequency of purchase. When we observe the Profit graph, we can see that Technology brings in the highest profit. But, the profit brought in by Furniture is very low considering that it has the second-highest sales, only a little different from Office Supplies. But, Office Supplies results in good profit.
# 
# Now, let's visualise the count plot for State.

# In[41]:


plt.figure(figsize=(20,8))
sns.countplot(df['State'], order = df['State'].value_counts().index, palette = 'plasma')

plt.title("Order Count for States")
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel("Count")
plt.show()


# We observe that California has the highest buyers, almost double New York, which has the second-highest buyers. Wyoming has the least buyers.
# 
# Let's check out the sales and profit for each state with the help of a double bar graph.

# In[57]:


state_sale_profit = df.groupby('State')[['Sales','Profit']].sum()
state_sale_profit.head()
state_sale_profit.sort_values('Sales', ascending= False, inplace= True)
state_sale_profit.head()
state_sale_profit.plot(kind="bar", figsize=(25,12), color=['darkviolet','dodgerblue'])
plt.title('sales/profit in each state')
plt.xticks(rotation=90)
plt.xlabel('state')
plt.ylabel('sales/profit')
plt.show()
state_sale_profit.head()


# We notice that quite a few of the states undergo an overall loss. Texas, which has the third-highest sales, witnesses a loss. Pennsylvania (fifth-highest sales) also witnesses a loss. Other states that witness a loss are; Florida, Illinois, Ohio, North Carolina, Arizona, Colorado, Tennessee.
# 
# California has the highest profit and a close second is New York.
# 
# Out of the top 10 states with the highest sales, 5 undergo an overall loss.
# 
# Let's observe the count plot for Sub-Categories.

# In[51]:


plt.figure(figsize=(20,8))
sns.countplot(df['Sub-Category'], order=df['Sub-Category'].value_counts().index, palette= 'plasma')
plt.title('Order-Count by Sub-category')
plt.xticks(rotation=90)
plt.xlabel('Sub-Category')
plt.ylabel('orders')
plt.show()


# In[60]:


subcategory_sale_profit = df.groupby('Sub-Category')[['Sales','Profit']].sum()
subcategory_sale_profit.sort_values('Sales', ascending=False, inplace=True)
subcategory_sale_profit.plot(kind="bar",color=["rebeccapurple","mediumpurple"],figsize=(20,8))
plt.title('Sales/Profit in each Sub-Category')
plt.xlabel('Category')
plt.ylabel('Sales/Profit')
plt.show()
 


# In[62]:


cat_sub_cat = df.groupby(['Category','Sub-Category'])[['Sales','Profit']].sum().reset_index()
cat_sub_cat


# We can see that while the sales for tables is the fourth-highest, it still undergoes the highest overall loss. Bookcases also witness a loss. Supplies witness the least loss. The profit incurred for machines is low.
# 
# Let's now observe the sales and profit of each sub-category separated by segment.

# In[63]:


sub_seg =df.groupby(['Sub-Category', 'Segment'])[['Quantity','Sales','Profit']].sum().reset_index()
sub_seg


# In[64]:


sns.catplot('Sub-Category', y='Sales', hue = 'Segment', data = sub_seg, kind='bar',palette='tab20c',aspect=2,height=8)
plt.title('Sub-Category Sales Segment-wise')
sns.catplot('Sub-Category', y='Profit', hue = 'Segment',data = sub_seg, kind='bar',palette='tab20c',aspect=2,height=8)
plt.title('Sub-Category Profit Segment-wise')
plt.show()


# The first plot represents the Sales and the second plot represents Profit. We can clearly see that tables undergo a loss in each segment. Bookcases and supplies undergo a loss in the Consumer segment.
# 
# Let's plot a scatter plot for Discount vs. Profit.

# In[65]:


plt.scatter(df['Discount'], df['Profit'])
plt.title('Discount vs. Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.show()


# We can observe that more the dicsount, lesser the profit.

# In[67]:


np.mean(df['Profit'])


# The average profit of the firm is 28.69, which is low. But,atleast the firm is not operating at a loss.

# # Inferences

#  1) In Shipping Modes, the most profitable and the most preferred shipping mode is the Standard Class. 
#  2) The Consumer Segment is the most profitable and has the most number of buyers.  
#  3) The Western region has the most sales and profit. However, the Central region has the least profit, and the Southern region has the least sales.
#  4) Office Supplies has the highest frequency of purchases. Technology has the most sales and is the most profitable. Furniture has the least profit although it has the second-highest sales.
#  5) Within Furniture, Tables in all segments undergoes heavy losses, and Tables also accounts for the highest loss amongst any other product. Bookcases in the Consumer segment witnesses losses.
#  6) In Office Supplies, Supplies undergoes a loss in the Consumer Segment.
#  7) In Office Supplies, Appliances has more sales in the Consumer segment than in the other segments. But the profit from Corporate segment is higher than that from Consumer segment.
#  8) In technology, although Machines have a pretty decent sales, the resultant profit is low. However, copiers and accessories compensate for that.
#  9) Out of the top 10 states with the highest sales, 5 undergo an overall loss. 
#  10) Texas, which has the third-highest sales, witnesses the highest loss.
#  11) The profit for both California and New York is more or less the same. But California has the highest sales, and New York the second highest. Therefore, we can say that for the same amount of sales, New York is more profitable.
#  12) A general observation is that more the sales, more the profit. 
#  13) More the discount, lesser the profit. 
#  14) The firm is operating at a low average profit of 28.69. But atleast it is not operating at a loss.

# # THANK YOU

# In[ ]:




