#!/usr/bin/python3
"""
0-subs.py
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    function method
    """
    response = requests.get('https://www.reddit.com/r/'
                            + subreddit + '/about.json')
    response.raise_for_status()
    data = response.json()
    if 'data' in data:
        return (data['data']['subscribers'])
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
