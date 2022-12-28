"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from utils import movies
import pickle
from thefuzz import process

movies = pd.read_csv('data/movies.csv') 
ratings = pd.read_csv('data/ratings.csv')
users = pd.read_csv('data/new_data.csv', index_col=0)


def recommend_random(k=10):
    return movies['title'].sample(k)


def recommend_with_NMF(k=10):
    
    with open('./nmf_recommender.pkl', 'rb') as file:
        model = pickle.load(file)
    
    #NMF Recommender
    #INPUT
    
    user_titles = request.args.getlist("title")
    user_ratings = request.args.getlist("rating")
    query = dict(zip(user_titles, user_ratings))
    #new_user = users.append(query, ignore_index=True)
    #new_user = user.fillna(value = 0)
    new_user = pd.DataFrame([[0]*users.shape[1]],columns=users.columns)
    new_user.loc[0,(query.keys())] = list(query.values())
    
    user_P = model.transform(new_user) 
    Q = model.components_
    user_R = np.dot(user_P,Q)

    recommendation = pd.DataFrame({ 'predicted_ratings':user_R[0]}, index = users.columns)
    recommendation = recommendation.sort_values(by=['predicted_ratings'],ascending=False)

    return recommendation[:k].index
    

def recommend_neighborhood(query, model, k=10):
    """
    Filters and recommends the top k movies for any given input query based on a trained nearest neighbors model. 
    Returns a list of k movie ids.
    """   
    pass
    

