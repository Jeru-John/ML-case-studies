# ML Case Study - Customer Churn Prediction in Telecom

## Project Overview

This project aims to build a predictive model to identify potential customers who have a higher probability of churning for a telecom company. By analyzing historical customer data, the company can develop focused customer retention programs to reduce churn and improve customer satisfaction.

## Data Description

The dataset contains customer information with various attributes, including churn status, services subscribed, customer account details, and demographic information. The goal is to predict the churn status of customers based on these attributes.

## Steps to the Project

1. **Import and Warehouse Data**

   - Import all the given datasets from the MYSQL server and explore the shape and size of each dataset.
   - Merge all datasets into one comprehensive dataset and explore the final shape and size.

2. **Data Cleansing**

   - Treat missing values in the dataset.
   - Convert categorical attributes to continuous using relevant functional knowledge.
   - Drop any irrelevant attributes using relevant functional knowledge.
   - Automate all the above data cleansing steps.

3. **Data Analysis & Visualization**

   - Perform detailed statistical analysis on the data.
   - Perform univariate, bivariate, and multivariate analysis with appropriate comments for each analysis.

4. **Data Pre-processing**

   - Segregate predictors vs. target attributes.
   - Check for target balancing and address any imbalanced classes.
   - Perform train-test split and ensure the train and test data have similar statistical characteristics.

5. **Model Training, Testing, and Tuning**

   - Train and test various ensemble models, including standard ensembles and custom ensemble techniques using weak classifiers.
   - Display the classification accuracies for train and test data.
   - Apply tuning techniques to find the best model for the data.
   - Compare and evaluate different models with their train and test accuracies.
   - Select the best-trained model with detailed comments on the selection process.
   - Serialize and save the selected model using Pickle for future use.

6. **Conclusion and Improvisation**

   - Summarize the results and findings from the project.
   - Provide suggestions for future data analysis, including improvements on data quality, quantity, variety, velocity, and veracity for better insights.

## Conclusion

This case study focuses on predicting customer churn in a telecom company. By using various ensemble models and tuning techniques, we have built a predictive model that can identify potential churners. The selected model has been serialized and saved for future use. The findings from the project will help the telecom company devise effective customer retention strategies.

## Improvements

For future data analysis, the telecom operator should consider collecting more data points to improve the accuracy of the churn prediction model. Additional data on customer behavior, customer feedback, and external factors can further enhance the predictive capabilities of the model. Additionally, continuous monitoring and updating of the model with new data will ensure its effectiveness in a dynamic business environment.

Please find the detailed analysis and code implementation in the respective notebooks located in the `notebooks/` directory.
