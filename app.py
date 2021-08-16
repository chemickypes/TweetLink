import article_parser
import hoo_tweet_link


def tweet_link(link):
    data = article_parser.parse_article(link)
    s = hoo_tweet_link.tweet(f"{data['title']}\n{' '.join(data['hashtags'])}\n{data['short_url']}")
    print(s)


if __name__ == '__main__':
    tweet_link('https://www.lintellettualedissidente.it/controcultura/societa/paradiso-delle-signore-rai-zola/')


