# Inventory-Analytics:

Introduction:

A data analytics project with Python and R aiming to automate the process of modeling an inventory's behavior given a dataset.
table of content:

- ABC(D) Classifier
- Visualization
- Demand Forecast 
- Replenishment Model

# Requirements and Dataset:

The project was built from scratch with Python 3.7 and R 1.2.5 and uses the traditional analytics libraries such as Numpy and Pandas and Matplotlib. Additionally it uses the Forecast library in R. 

The dataset used for this project can be found at https://docs.lokad.com/getting-started/the-sample-dataset/. It includes fives years of data of about 95 SKU's, demand data and supplier purchase data. 


# 1- ABC(D) Classifier:

A program that classify the SKU's within classes based on their invidual added value to the total inventory value. Within classes, SKU's are classified in categories and sub-categories of products. 

- classAA : Top performing SKU's, they generate 40% of the total revenue. 
- classA: Well performing SKU's that account for the next 40% of the total revenue.
- classB: Includes the regular items, representing the next 10% of the inventory revenue.
- classC: Following 8% of the SKU's, they are either slow movers or non performing items.
- classD: Last 2% of the items, they are the NON- performing items. 

# Visualization: 

A script that shows the behavior of the inventory and the demand through a series of plots. Being able to visualize the behavior of the inventory greatly increases the chances of making meaningful and accurate management decisions.

- evolution of the total demand over the 5 years of historical data. 
- Historical yearly evolution of the demand each year. 
- graphical representation of the inventory behavior dividing, aiming to clasifiy SKU's in frequency of sales within a week compared to the mean average performing item. 


# Forecast:

The demand for each SKU is forecasted using the ARIMA method and the STL method. The data is ran through each forecast method and select the one witht the smallest MAPE error. 

Predictions for each SKU are made of a 8 weeks horizon. 

# Replenishment Model:

a program that gets the prediction data from R and calculates the mean and standard deviation of each demand for each SKU. From there, the inventory is modeled based on the ABCD classifier. Because the dataset is about a retail organization, replenishment is based on service-level (TSL). 

- classAA TSL: 98.5%
- classA TSL: 97.5%
- classB TSL: 95%
- classC TSL: 93%
- classD TSL: 0.90%

The program calculates the re-order point and the safety stock necessary for all the SKU's.



# Summary: 

In more details, this projects aims to automate the analytics of inventory through providing basic tools to understand the behavior of the inventory as well as the behavior of the demand. From those insights, a prediction model calculates demand for a given forecast horizon. From the demand forecast, re-order point and safety stock is calculated. 










