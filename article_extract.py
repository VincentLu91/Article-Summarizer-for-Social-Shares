import requests
from bs4 import BeautifulSoup
import nltk
import networkx as nx
import numpy as np
import pandas as pd
nltk.download('punkt') # one time execution
from nltk.corpus import stopwords
import re
from sklearn.metrics.pairwise import cosine_similarity
from summa import summarizer
from summa.summarizer import summarize

# function to remove stopwords
def remove_stopwords(sen):
    stop_words = stopwords.words('english')
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

def convert_article_text_to_paragraphs(article_link):
    the_url = requests.get(article_link).text
    soup = BeautifulSoup(the_url,'html.parser')

    title = soup.title
    article_headline = soup.find('h1',{'class':'article__headline'})

    list_of_paragraphs = []
    for strong_tag in soup.find_all('p'):
        list_of_paragraphs.append(strong_tag.text)

    paragraphs = ''.join(list_of_paragraphs)
    return paragraphs
'''
# pagerank implementation
def summarize_article_pr(article_link):
    paragraphs = convert_article_text_to_paragraphs(article_link)

    # from here, split text to sentences:
    list_of_sentences = nltk.tokenize.sent_tokenize(paragraphs)

    # Extract word vectors
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefficients = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefficients
    f.close()

    len(word_embeddings)

    # process text
    clean_sentences = pd.Series(list_of_sentences).str.replace("[^a-zA-Z]", " ")

    clean_sentences = [s.lower() for s in clean_sentences]

    stop_words = stopwords.words('english')

    clean_sentences = [remove_stopwords(clean_sentence.split()) for clean_sentence in clean_sentences]

    # create sentence vectors:
    sentence_vectors = []
    for clean_sentence in clean_sentences:
        if len(clean_sentence) != 0:
            vec = sum([word_embeddings.get(w, np.zeros((100,))) for w in clean_sentence.split()])/(len(clean_sentence.split())+0.001)
        else:
            vec = np.zeros((100,))
        sentence_vectors.append(vec)

    # initialize the empty similarity matrix
    similarity_matrix = np.zeros([len(list_of_sentences), len(list_of_sentences)])

    # now, initialize the similarity matrix with cosine similarity scores - similarity between sentences
    for i in range(len(list_of_sentences)):
        for j in range(len(list_of_sentences)):
            if i != j:
                similarity_matrix[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0][0]

    # with the similarity matrix, convert it to a graph:
    nx_graph = nx.from_numpy_array(similarity_matrix)

    # apply pagerank algorithm on the graph that was converted from similarity matrix:
    pr = nx.pagerank(nx_graph)

    # extract the sentences ranked in descending order
    ranked_sentences = sorted(((pr[i],s) for i,s in enumerate(list_of_sentences)), reverse=True)
    
    # initialize list of top 10 sentences as a summary:
    summaries = []

    # Extract top 10 sentences as the summary
    for i in range(len(ranked_sentences)):
        summaries.append(ranked_sentences[i][1])
    
    return summaries
'''
# textrank implementation with summa summarizer
def summarize_article_tr(article_link):
    paragraphs = convert_article_text_to_paragraphs(article_link)
    summaries = summarize(paragraphs, split=True, ratio=0.2)
    return summaries