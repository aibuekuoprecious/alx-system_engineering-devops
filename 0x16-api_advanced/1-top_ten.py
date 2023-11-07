#!/usr/bin/python3
"""
Script that prints out top ten hottest posts
of a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    api_url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "Mozilla/5.0"
    limit = 10

    response = requests.get(
        api_url, headers={"user-agent": user_agent}, params={"limit": limit}
    )
    if not response:
        print("None")
        return

    response_data = response.json()
    posts = response_data["data"]["children"]

    for post in posts:
        print(post["data"]["title"])
