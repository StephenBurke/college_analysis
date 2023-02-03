from flask import Flask
import numpy as np
import pandas as pd
import pickle
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

# Members API Route


@app.route("/members")
def members():
    return {"members": ["Member_1", "Member_2", "Member_3"]}


if __name__ == "__main__":
    app.run(debug=True)

# returns school recommendations... in a way


def prep_recommendations(index):
    # ! requires outside data => need to clean
    # requires cos_sim_data and df_vector
    global index_recommend
    global college_recommend

    index_recommend = cos_sim_data.loc[index].sort_values(
        ascending=False).index.tolist()[1:6]
    college_recommend = df_vector['organizationName'].loc[index_recommend].values
    result_p = {'School': college_recommend, 'Index': index_recommend}

    return result_p

# returns school name


def get_school(index):

    return df_vector['organizationName'].loc[index]

# returns school description


def get_description(index):

    return df_vector['description'].loc[index]

# returns a list of school recommendations


def get_school_recommendations():

    school_array = [college for college in college_recommend]
    return school_array

# returns a list of school recommendation descriptions


def get_school_recommendation_desc():

    desc_array = []
    for q in range(len(college_recommend)):
        desc_q = df_vector['description'].loc[index_recommend[q]]
        desc_array.append(desc_q)

    return desc_array


# load pd from pickle
df_vector = pd.read_pickle('./flask-server/df_vector.pkl')

# load row_list data
with open('./flask-server/df_rows.bin', 'rb') as f:
    row_data = pickle.load(f)

# list of schools
schools = df_vector['organizationName'].unique()

# create vectorized lists
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(row_data)

# find cosine similarities
cos_sim_data = pd.DataFrame(cosine_similarity(X))

prep_recommendations(random.randint(0, len(schools)))
