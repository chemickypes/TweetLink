import article_parser
import hoo_tweet_link


def tweet_link(link):
    data = article_parser.parse_article(link)
    return hoo_tweet_link.tweet(f"{data['title']}\n{' '.join(data['hashtags'])}\n{data['short_url']}")


if __name__ == '__main__':
    s = tweet_link('https://www.tutorialkart.com/python/python-datetime/python-datetime-format/')
    print(s)


