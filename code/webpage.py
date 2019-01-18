from flask import Flask, render_template, jsonify, request
import requests
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import ast
import pickle
app = Flask(__name__)


# posts = [
#     {
#         'author': 'Sunny',
#         'title': 'headline 1',
#         'content': 'blah blah blah',
#         'url': 'www.google.com',
#         'date_posted': 'January 1, 2019'
#     },
#     {
#         'author': 'Hunter',
#         'title': 'headline 2',
#         'content': 'I am a snowflake',
#         'url': 'www.google.com',
#         'date_posted': 'January 2, 2019'
#     }
# ]
# import pandas as pd
# posts_df = pd.DataFrame(posts, columns = posts[0].keys())

# references index.html file
@app.route("/")
@app.route("/index")
def main_page():
    return render_template('index.html', title='Foobar')

# # references home.html file
# @app.route("/home")
# def home():
#     return render_template('home.html')

@app.route("/json", methods=['POST'])
def json_route():
    # user input search term
    search_term = request.form['selection']

    # get news using News API
    url = 'https://newsapi.org/v2/everything?'
    param = {
        'q'        : search_term,
        'apiKey'   : 'e685d6e1420f4882b86d029ed3c1a11d',
        'pageSize' : 100,
        'language' : 'en',
        'sortBy'   : 'relevancy',
        'page'     : 1
        }

    data = []
    for page in range(1, 11):
        param['page'] = page
        response = requests.get(url = url, headers = {'User-agent': 'Infinity browser'}, params = param)
        json = response.json()['articles']
        data.extend(json)

    # Build dataframe
    df_temp = pd.DataFrame(data)
    df_temp.drop(['author', 'publishedAt', 'source', 'urlToImage'], axis=1, inplace=True)
    df_temp['text'] = df_temp['title'] + df_temp['description'] + df_temp['content']

    model_dict = {
        'wildfire': '../pickles/wildfire_2.pk',
        'earthquake': '../pickles/earthquake_2.pk',
        'flood' : '../pickles/flood_2.pk'
    }

    vect_dict = {
        'wildfire': '../pickles/wildfire_vect.pk',
        'earthquake': '../pickles/earthquake_vect.pk',
        'flood': '../pickles/flood_vect.pk'
    }

    # Load in pickled objects
    vect = pickle.load(open(vect_dict[search_term], 'rb'))
    model = pickle.load(open(model_dict[search_term], 'rb'))

    # Transform data using fit vectorized object
    X = vect.transform(df_temp['text'].dropna()).toarray()
    tfidf = pd.DataFrame(X, columns = vect.get_feature_names())

    # Tranform vectorized data using LDA and get out relevant documents
    comp = model.transform(tfidf)
    document_topics = pd.DataFrame(comp, columns=["topic %d" % i for i in range(comp.shape[1])])
    top_topics = (document_topics['topic 1'] > .3)
    docs = document_topics[top_topics].index

    df = df_temp.loc[docs]
    df.drop(['content', 'text'], axis=1, inplace=True)

    posts = ast.literal_eval(df.to_json(orient='records'))
    return render_template('disaster.html', posts = posts, title='blah')


# Allows us to dynamically update webpage without having to quit the flask server
if __name__ == '__main__':
    app.run(debug=True)
