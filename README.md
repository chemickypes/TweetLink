# TweetLink
Client Twitter for link

A simple python software to analyze a link, extract hashtag and tweet all generated data

## How To use
You can download and execute.
Notice: you have to write a `secrets.py` file with:

``` python
cuttly_api_key = "..."

twitter_access_token = "..."
twitter_secret_token = "..."

twitter_consumer_api_key = "..."
twitter_consumer_secret_key = "..."
```

* [Cuttly](https://cutt.ly/) Url Shortener
* [Twitter Dev](https://developer.twitter.com/): You have to create you app and you access

## Data Analizer Algorithm 
Algorithm to extract hashtags is so simple:
* get all text
* remove stopwords (english or italian)
* count the word occurrences and select the first 4 words

### TODO
* IDEA - Analyze the word type to select nouns and avoid verbs 
