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
from short_url import short_link_of

license_console = """TweetLink  Copyright (C) 2021  Angelo Moroni
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details."""


def tweet_link(link):
    data = article_parser.parse_article(link)
    short_url = short_link_of(link)
    return hoo_tweet_link.tweet(f"{data['title']}\n{' '.join(data['hashtags'])}\n{short_url}")


if __name__ == '__main__':
    print(license_console)
    link = input('Type link to tweet:')
    s = tweet_link(link)
    if 'created_at' in s:
        print("twitted at {}".format(s['created_at']))
    else:
        print(s['error'])
