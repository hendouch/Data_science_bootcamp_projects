# Data_science_projects

## 01_visual_data_analysis_animated_scatterplot

This animated scatterplot visualizes the changes of countries' fertility rate, life expectancy and population between 1960 and 2015. The sizes of the scatters represents the population of each country, the colours shows in which continent they can be found.

## 02_classification_titanic_challange

The goal of this project was to built a machine learning model to predict the survival of Titanic passenger based on the features in the dataset of Kaggle's "Titanic - Machine Learning from Disaster".

Based on the Exploratory Data Analysis (plotted missing values and the correlation between survival and the different data categories) selected the most significant features and dropped the ones which cannot contribute to accurate prediction. In feature engineering using ColumnTransformer, I applied 1) OneHotEncoder: to convert categorical variables into binary features, 2) SimpleImputer: to fill missing values and 3) MinMaxScaler: to normalize continous numerical variable in range 0.0 - 1.0. The data was trained on Scikit-learn's LogisticRegression and RandomForestClassifier models. After evaluating different model's accuracy scores and cross validation, I kept the LogisticRegression model for prediction (cross validation: mean accuracy score 81.28 +- 3.98 %).

## 03_regression_bycicle_rental_prediction

The goal of this project was to build a regression model, in order to predict the total number of rented bycicles in each hour based on time and weather features, optimizing the accuracy of the model for RMSLE, using Kaggle's "Bike Sharing Demand" dataset that provides hourly rental data spanning two years.

After extracting datetime features, some highly correlated variables were dropped via feature selection (correlation analysis, Variance Inflation Factor) to avoid multicollienarity. I compared more linear regression models with one another (PossionRegressor, PolinomialFeatures, Lasso, Ridge, RandomForestRegressor) based on R2 and RMSLE scores. After evaluating the different models, I kept the RandomForestRegressor, and applied GridSearchCV and cross validation to ensure the best fit, finally submitted the predictions with 0.47210 RMSLE.

## 04_nlp_text_classification

The main goal of this project was to build a text classification model on song lyrics to predict the artist from a piece of text, additionally, to make user-inputs (artists, lyrics) possible in CLI.

Through web scraping with BeautifulSoup, the song-lyrics of selected artists are extracted from lyrics.com. During the text pre-processing, word-tokenizer and word-lemmatizer of Natural Language Toolkit (NLTK) is used to "clean" the extracted texts and create the corpus: 1) TreebankWordTokenizer() splits the text into list of words and removes all other punctuation marks, 2) WordNetLemmatizer() reverts words back to their root/base. These steps are required to import and download lexical database such as WordNet. WordNet's Stopwords also removes the most common English words from the corpus.

In the model pipeline, Tfidfvectorizer (TF-IDF) transforms the words of the corpus into a matrix, count-vectorizes and normalizes them at once by default. For classification, the multinomial Naive Bayes classifier MultinomialNB() was used which is suitable for classification with discrete features like word counts for text classification.

## 05_data_pipeline_tweets_sentiment_analysis

The challenge of this Data Engineering project was to build a Dockerized Data Pipeline to analyze the sentiment of tweets. At first, using Tweepy API, tweets are collected in a selected topic and stored in a MondoDB database (tweet_collector). Next, the sentiment of tweets is analyzed and the tweets with the scores are stored in a Postgres database (ETL_job). Finally, tweets with sentiment score are published on a Slack channel. (slack_bot)

For the sentiment analysis, SentimentIntensityAnalyzer() of the the Vader library (Valence Aware Dictionary and sEntiment Reasoner) was used.

## 06_time_series_temperature_forecast

In this project, I applied the ARIMA model for a short-term temperature forecast. After visualizing the trend, the seasonality and the remainder of the time series data (daily mean temperature in Berlin-Treptow from 1979-2020), I run tests such as ADF and KPSS for checking stationarity (time dependence).

For determining the parameters of the ARIMA model (p, d, q), I present two approaches:

Inspecting the lags of the Autocorrelation (ACF) and Partial Auto Correlation Functions (PACF) plots.
Using alkaline-ml Auto-Arima process which automatically finds the most optimal order setting that has the lowest AIK.
The prediction with the tuned ARIMA model achieved a MAE score as low as 1.72.

## 07_mcmc_predicting_customer_behaviour

The goal of this project was to predict and visualize customer behaviour between departments/aisles in a supermarket, applying Markov Chain modeling and Monte-Carlo simulation.

The project included the following tasks:

Data Analysis
Calculating Transition Probabilities between the aisles
Implementing a Customer Class
Running MCMC (Markov-Chain Monte-Carlo) simulation for a single class customer
Extending the simulation to multiple customers
Animation/Visualization

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
