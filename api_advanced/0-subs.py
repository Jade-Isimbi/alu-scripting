#!/usr/bin/python3

"""
A module to fetch and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if an error occurs.
    """
    # Define the User-Agent header to avoid request blocking by Reddit
    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    # Construct the URL to query Reddit's API for the subreddit's details
    URL = f"https://api.reddit.com/r/{subreddit}/about"
    try:
        # Send a GET request to the API with the specified headers
        response = requests.get(URL, allow_redirects=False,
                                headers={'User-Agent': USER_AGENT}).json()
        # Extract and return the number of subscribers from the response
        return response.get("data", {}).get("subscribers", 0)
    except Exception:
        # Return 0 in case of any errors
        return 0


if __name__ == "__main__":
    import sys

    # Check if a subreddit name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call the function with the provided subreddit name and print the result
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

