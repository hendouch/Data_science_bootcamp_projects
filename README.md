# Data_science_projects

## 01_visual_data_analysis_animated_scatterplot

This animated scatterplot visualizes the changes of countries' fertility rate, life expectancy and population between 1960 and 2015. The sizes of the scatters represents the population of each country, the colours shows in which continent they can be found.

## 02_classification_titanic_challange

The goal of this project was to built a machine learning model to predict the survival of Titanic passenger based on the features in the dataset of Kaggle's "Titanic - Machine Learning from Disaster".

## 03_regression_bycicle_rental_prediction

The goal of this project was to build a regression model, in order to predict the total number of rented bycicles in each hour based on time and weather features, optimizing the accuracy of the model for RMSLE, using Kaggle's "Bike Sharing Demand" dataset that provides hourly rental data spanning two years.

## 04_nlp_text_classification

The main goal of this project was to build a text classification model on song lyrics to predict the artist from a piece of text, additionally, to make user-inputs (artists, lyrics) possible in CLI.

Through web scraping with BeautifulSoup, the song-lyrics of selected artists are extracted from lyrics.com. 

In the model pipeline, Tfidfvectorizer (TF-IDF) transforms the words of the corpus into a matrix, count-vectorizes and normalizes them at once by default. For classification, the multinomial Naive Bayes classifier MultinomialNB() was used which is suitable for classification with discrete features like word counts for text classification.

## 05_data_pipeline_tweets_sentiment_analysis

The challenge of this Data Engineering project was to build a Dockerized Data Pipeline to analyze the sentiment of tweets. At first, using Tweepy API, tweets are collected in a selected topic and stored in a MondoDB database (tweet_collector). Next, the sentiment of tweets is analyzed and the tweets with the scores are stored in a Postgres database (ETL_job). Finally, tweets with sentiment score are published on a Slack channel. (slack_bot)

For the sentiment analysis, SentimentIntensityAnalyzer() of the the Vader library (Valence Aware Dictionary and sEntiment Reasoner) was used.

## 06_time_series_temperature_forecast

In this project, I applied the ARIMA model for a short-term temperature forecast. After visualizing the trend, the seasonality and the remainder of the time series data (daily mean temperature in Berlin-Treptow from 1979-2020), I run tests such as ADF and KPSS for checking stationarity (time dependence).

For determining the parameters of the ARIMA model (p, d, q), I present two approaches:

Inspecting the lags of the Autocorrelation (ACF) and Partial Auto Correlation Functions (PACF) plots.

## 07_mcmc_predicting_customer_behaviour

The goal of this project was to predict and visualize customer behaviour in a supermarket, applying Markov Chain modeling and Monte-Carlo simulation.

The project included the following tasks:

Data Analysis
Calculating Transition Probabilities between the aisles
Implementing a Customer Class
Running MCMC (Markov-Chain Monte-Carlo) simulation for a single class customer
Extending the simulation to multiple customers

## 08_deep_learning

The goal of this project was to build an Artificial Neural Network that recognizes objects on images made by the webcam:

The project included the following tasks:

Implementing a Feed-Forward Neural Network
Backpropagation from Scratch
Building Neural Network with Keras
Training Strategies / Hyperparameters of Neural Networks
Convolutional Neural Networks (CNN)
Classifying images made with webcam with Pre-trained Networks (Comparing MobileNetV2, InceptionV3)
Image Detection

## 09_recommender_system

The movie recommender is based on the Collaborative Filtering approach, and creates predictions for movie ratings with Matrix Factorization technique, more precisely, the SVD (Singular Value Decomposition) algorythm of the SurPRISE library. It is trained on 'small' dataset of MovieLens.
