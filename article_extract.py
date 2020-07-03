import requests
from bs4 import BeautifulSoup
from summa import summarizer
from summa.summarizer import summarize

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

# textrank implementation with summa summarizer
def summarize_article_tr(article_link):
    paragraphs = convert_article_text_to_paragraphs(article_link)
    summaries = summarize(paragraphs, split=True, ratio=0.2)
    return summaries