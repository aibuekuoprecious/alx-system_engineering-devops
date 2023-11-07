#!/usr/bin/python3
"""
Script that returns the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit
    """

    api_url = f"https://reddit.com/r/{subreddit}/about.json"
    user_agent = "Mozilla/5.0"

    response = requests.get(api_url, headers={"user-agent": user_agent})
    if not response:
        return 0

    subscribers = response.json().get("data").get("subscribers")
    if subscribers:
        return subscribers
    else:
        return 0
