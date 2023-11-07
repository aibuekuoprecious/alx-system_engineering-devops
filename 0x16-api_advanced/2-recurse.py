#!/usr/bin/python3
"""
Fetch all hot articles recursively
"""

import requests


REDDIT_BASE_URL = "https://www.reddit.com/"
USER_AGENT = {'user-agent': 'my-app/0.0.1'}


def recurse(subreddit,  hot_list=[], next_page_token=""):
    """
    Recursively fetches the titles of all hot articles for a given subreddit.
    """

    if next_page_token is None:
        return  hot_list

    api_url = REDDIT_BASE_URL + "r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': next_page_token
    }

    response = requests.get(api_url, headers=USER_AGENT, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        json_data = response.json()
    except ValueError:
        return None

    try:
        data = json_data.get("data")
        next_page_token = data.get("after")
        posts = data.get("children")

        for post in posts:
             hot_list.append(post.get("title"))

    except Exception:
        return None

    return recurse(subreddit,  hot_list, next_page_token)
