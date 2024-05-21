# House Price Prediction

This project implements machine learning algorithms to predict house prices based on various features such as number of bedrooms, number of bathrooms, size of the house, and zip code. It includes data preprocessing, model training, and evaluation using techniques like Linear Regression, Lasso Regression, and Ridge Regression.

## Overview

House price prediction is a common problem in the real estate industry and has significant implications for buyers, sellers, and real estate agents. Accurately predicting house prices can help buyers make informed decisions, sellers set appropriate listing prices, and agents provide valuable insights to their clients.

As part of this project, I explored the impact of different regression techniques on the predictive performance of the models. The dataset used in this project contains information about various houses including their features and corresponding prices.

## Algorithms Used

- **Linear Regression**: This algorithm predicts house prices using a linear relationship between the features and the target variable.
- **Lasso Regression**: Lasso Regression applies L1 regularization to the model, which helps in feature selection and prevents overfitting.
- **Ridge Regression**: Ridge Regression applies L2 regularization to the model, which helps in reducing the impact of multicollinearity.

## Project Structure

- `data/`: Contains the dataset used for training and testing.
- `models/`: Saved models trained during the project.
- `notebooks/`: Jupyter notebooks used for data analysis and model training.
- `src/`: Source code files including data preprocessing, model training, and evaluation.
- `requirements.txt`: Dependencies required to run the project.
