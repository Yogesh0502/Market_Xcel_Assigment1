# Market_Xcel_Assigment1
How to Run:
Clone the Repo and then run in CMD
$ python app.py

Problem Statement: 
1.   Use the attached dataset "Assignment 1_sales data.csv" for ETL.
2.   Write code for checking the data for outliers, missing values and if there are many, impute them.
3.   Create a model to predict the Quantity and Amount using the provided data.
4.   Create a webapp where the user can input city, brand, model name, RAM and internal memory to predict Quantity and Amount.
5.   Please provide the working script for all the above points.

Date: Assignment 1_sales data.csv

Solution: Model2.pkl
Detaile of model is in Base_Model.ipynb

Approach: Used Random forest Regressor to predict the Amount. 
Used Flask to create Webapp.

Conclusion from the EDA:
1. Looking at the data closely I found that the Items with missing RAM and Memory have relatively low price.
and those item having RAM and Memory but still have low price are having Amount higher. 
So, created a sepearte class for missing RAM and Memory and make it as Default.

2. Confirmed that, each Brand has different Model number.
So, no 2 brand has same model.

3. As Serial number increases, total sum of order is decreasing.

4. Model Name is not affecting the accuracy that much. So, droped Model feature.

5. Price/Unit is not included in the Prediction of Amount as the relation between Amount and Price/Unit is
Price/Unit * Quantity = Amount
and Quantiy taken is 1 in the prediction.
So, prediction of Price/Unit is same as prediction of amount

6. For Quantity > 1, there are only 10 data points which is not enough for the prediction. So, dropped them 
and Predicted only for 1 Quantity.
