# Article Summarizer for Social Shares

The article summarizer generates potential social media posts - each with a summary and an article link. It uses the implementation of TextRank from the [summanlp](https://github.com/summanlp/textrank) library. It uses extractive text summarization.

The user can enter any long form article URL and the TextRank algorithm generate all possible summaries. Each summary contains a sentence (largely verbatim from source article) that attempts to explain a high level idea of the article along with the article URL that the user entered. The user could then use any of all the summaries to post them on their social media feed - such as Facebook and LinkedIn.

One limitation of this data app is that the summaries can be of any length so it may not always be suitable for sharing on platforms like Twitter, which enforces the limit of 140-characters. Another limitation is that the outputs of the app are for textual social sharing, so it does not apply to visual platforms such as Instagram or Snapchat.

I have written a blog post on the topic: https://vincentlu91.github.io/2020/06/29/article-summary-for-social-sharing.html

## How to access the data app

### Deployed App

You can use the following link here: https://technical-summary-proj.herokuapp.com

### Alternatively, you can access the application in development environment

Libraries and their versions are included in requirements.txt. To install the virtual environment, run the following:

```
python3 -m venv env # or python -m venv env
source env/bin/activate
pip3 install -r requirements.txt # or pip install -r requirements.txt
```

At this point the environment should be set up with required libraries to run the application. To run the app, enter:
```
python app.py
```

Then in the browser, enter ```localhost:5000```

## How to use the data app

You will see a prompt to enter the article URL. The field validates if the input given fits the pattern of a URL or not.

![martymcfly](https://user-images.githubusercontent.com/3411100/86504539-86525a00-bd87-11ea-851d-e0c2fc65de75.png)

It prompts for an article link. For example, suppose the link is a Wikipedia article on Principal Component Analysis:
https://en.wikipedia.org/wiki/Principal_component_analysis

Here is the result:

![martymcfly](https://user-images.githubusercontent.com/3411100/86504589-260fe800-bd88-11ea-8693-e29e4909789a.png)
