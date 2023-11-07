#!/usr/bin/python3
""" Count it! """
from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def count_words(subreddit, keywords, pagination_token="", keyword_counts={}):
    """
    Recursive function that queries the Reddit API, parses the title 
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    """
    if not keyword_counts:
        for keyword in keywords:
            keyword_counts[keyword] = 0

    if pagination_token is None:
        keyword_counts = [[key, value] for key, value in keyword_counts.items()]
        keyword_counts = sorted(keyword_counts, key=lambda x: (-x[1], x[0]))
        for keyword_count in keyword_counts:
            if keyword_count[1]:
                print("{}: {}".format(keyword_count[0].lower(), keyword_count[1]))
        return None

    url = REDDIT + "r/{}/hot/.json".format(subreddit)
    params = {
        'limit': 100,
        'after': pagination_token
    }

    resp = get(url, headers=HEADERS, params=params, allow_redirects=False)
    if resp.status_code != 200:
        return None

    try:
        js = resp.json()
    except ValueError:
        return None

    try:
        data = js.get("data")
        pagination_token = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            post_title = post.get("title")
            lowercase_words = [s.lower() for s in post_title.split(' ')]
            for keyword in keywords:
                keyword_counts[keyword] += lowercase_words.count(keyword.lower())
    except:
        return None

    count_words(subreddit, keywords, pagination_token, keyword_counts)