#!/usr/bin/python3
"""
0-subs.py
"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """
    0-subs.py
    """
    head = {'User-Agent': 'Mozilla/5.0'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=head).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
