from flask import Flask, render_template, request
from recommender import recommend_random,recommend_with_NMF
from utils import movies
import pickle

with open('./nmf_recommender.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html',name='Henda',movies = movies.title.to_list())
@app.route('/recommendation')
def random_recommendation():
    titles = request.args.getlist("title")
    ratings = request.args.getlist("rating")
    user_rating = dict(zip(titles, ratings))

    #print(titles, ratings)

    
    for keys in user_rating:
        user_rating[keys] = int(user_rating[keys])

    #print(user_rating)
    if request.args['method'] == 'Random':
        recs = recommend_random(k=10).to_list()
        return render_template('recommender.html',values = recs)
    if request.args['method'] == 'NMF':
        recs = recommend_with_NMF(k=10)
        return render_template('recommender.html',values = recs)
    else:
        return 'Fuction not defined' 
    

if __name__=='__main__':
    app.run(port=5000,debug=True)