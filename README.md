# technical_summary_proj

The article summarizer is made to produce potential social media posts with a summary and the article link. It uses two approaches - the ['PageRank'](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/) implementation of TextRank and the [summanlp](https://github.com/summanlp/textrank) library.

The user can enter any long form article URL and select either one of two TextRank implementations to generate summaries. Each summary contains the text that attempts to explain a high level idea of the article along with the article URL that the user entered so they could copy and paste share on social media platforms - namely Facebook and LinkedIn. 

The limitation of this data app is that the summaries can be of any length so it may not always be suitable for sharing on Twitter given the 140-character constraint on posting tweets.
