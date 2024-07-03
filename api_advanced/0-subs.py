#!/usr/bin/python3

"""
A simple script to fetch and print the number of subscribers for a given subreddit.
"""

import requests

def sub_counter(sub_reddit):
    """
    Fetches the number of subscribers for a given subreddit.

    Args:
        sub_reddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if an error occurs.
    """
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    URL = f"https://api.reddit.com/r/{sub_reddit}/about"
    try:
        response = requests.get(URL, allow_redirects=False, headers={'User-Agent': USER_AGENT}).json()
        return response.get("data").get("subscribers")
    except Exception:
        return 0
