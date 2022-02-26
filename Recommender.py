#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

def data_prep(data):
    df = data[['user_id','item_id','purhased']]
    df_grouped = df.groupby(['user_id','item_id']).sum().reset_index()
    for i in range(len(df_grouped.purchased)):
        if df_grouped.iloc[i,-1] > 1:
            df_grouped.iloc[i,-1] = 1
    return df_grouped

def cos_similarity(user_ids, item_ids):
    item_user_matrix = csr_matrix(([1]*len(user_ids), (item_ids, user_ids)))
    similarity = cosine_similarity(item_user_matrix) #creates a cosine similarity martix
    return similarity, item_user_matrix

def get_recommendations_item_user(similarity, item_user_matrix, top_n=10):
    user_item_matrix = csr_matrix(item_user_matrix.T)
    user_item_score = user_item_matrix.dot(similarity) # sum of similarities to all purchased items to create a score
    recom = []
    for user_id in range(user_item_score.shape[0]):
        scores = user_item_score[user_id, :]
        purchased_items = user_item_matrix.indices[user_item_matrix.indptr[user_id]:user_item_matrix.indptr[user_id+1]]
        scores[purchased_items] = -1 # do not recommend already purchased items
        top_item_ids = np.argsort(scores)[-top_n:][::-1]

        recommendations = pd.DataFrame(top_item_ids.reshape(1, -1),index=[user_id],columns=['Top%s' % (i+1) for i in range(top_n)])
        recom.append(recommendations)
        
    return pd.concat(recom) 

def get_recommendations(data_grouped):
    # compute recommendations
    similarity_matrix, item_user_matrix = cos_similarity(data_grouped.user_id, data_grouped.item_id)
    recommendations = get_recommendations_item_user(similarity_matrix, item_user_matrix)
    return recommendations

path = input("Enter dataset path: ")
data = pd.read_csv(path)
df_grouped = data_prep(data)
recommendations = get_recommendations(df_grouped)
for_excel = recommendations
for_excel.to_excel("Recommendations_by_Customers.xlsx")

