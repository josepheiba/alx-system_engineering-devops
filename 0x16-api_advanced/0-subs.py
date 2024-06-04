#!/usr/bin/python3
"""Function ro retrieve the number of subscribers for a specific subreddit."""
import requests


def number_of_subscribers(subreddit):
    """queries the subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        # "Users-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        "User-Agent": "linux:0x16.api.advanced"

    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
