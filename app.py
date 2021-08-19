"""
 Copyright (C) 2021  Angelo Moroni

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import article_parser
import hoo_tweet_link


def tweet_link(link):
    data = article_parser.parse_article(link)
    return hoo_tweet_link.tweet(f"{data['title']}\n{' '.join(data['hashtags'])}\n{data['short_url']}")


if __name__ == '__main__':
    s = tweet_link('https://www.tutorialkart.com/python/python-datetime/python-datetime-format/')
    print(s)


