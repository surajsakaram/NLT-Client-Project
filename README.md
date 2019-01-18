# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Leveraging News and Media for Situational Awareness.

### Problem Statement   
   
During a major disaster, it is essential to provide the public and responders with relevant local news updates in order to gain situational awareness during the event.
During a disaster, news updates are coming from tens to hundreds of different sources, all in different formats, available from different websites, news channels etc., and it is often difficult to find what would be most helpful amid the chaos of other non-disaster related news and media.
There is currently no forum for rounding up and archiving relevant news for a live disaster event.
This project will leverage news feeds relevant to specific disasters, gathered from multiple sources, to create a webpage that presents these live feeds under one umbrella (on one page). This is similar to the Google News feature.


## The process.

We used News API to collect 1000 most relevant articles for the past 12 months about ‘wildfire’, ‘earthquake’ and ‘flood’ in english from over 30 000 news sources from all over the world.
This API allows us to obtain important information about each news article including: content, title, short description, author, and URL.
Then using the combination of content, description and title of each article for specific category of disaster we transformed them using TF-IDF Vectoriser, deleted stop words. We used Latent Dirichlet Allocation (LDA) model to create some amount of topics, based on the relationships between words in each article.
Then we chose the most disaster--related topic and filtered out all the articles that not fit into that specific topic and we put disaster-related articles to the webpage using Flask (Python Microframework application).

### Conclusions and Recommendations

This is the test version of this product (or trial version, if you like). In order to create more sophisticated and precise versions of the filtering models we will use more NLP techniques combined with LDA or without LDA, we will create complex customized models for every name of every possible disaster, so we can sort all the articles with precision of 100%. Using the most modern achievements of Machine Learning. Also we can create extraordinary public website with lot of different options, very user friendly and easy navigation. But to do that our team would need more resources
