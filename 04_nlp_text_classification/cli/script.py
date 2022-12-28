import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB  
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_extraction.text import CountVectorizer

df=pd.read_csv('week_4/lyrics.csv')
ldf=df.dropna()
ldf1=ldf.drop_duplicates()
df['Artist_name'].value_counts()
df['Artist_name'].value_counts(normalize=True) * 100
corpus = ldf1['Lyrics']
labels = ldf1['Artist_name'] 
corpus = [s.lower() for s in corpus]


def train_naive_bayes(corpus, labels):
    tf_vec = TfidfVectorizer()
    nb = MultinomialNB(alpha = 1)
    model = make_pipeline(tf_vec, nb)
    model.fit(corpus, labels)
    
    return model
 

def predict_naive_bayes(model, new_text):
    new_text = [new_text]
    prediction = model.predict(new_text)
    probabilities = model.predict_proba(new_text)
    
    return prediction[0], probabilities






y_true = ldf1['Artist_name']
X_test = "We love a loyal submarine"




if __name__ == "__main__":
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import make_pipeline
    import pickle

    NB_clf = train_naive_bayes(
        corpus = corpus,
        labels = labels
    )

with open("week_4/cli/naive_classifier.bin", "wb") as file:
    pickle.dump(NB_clf, file)

