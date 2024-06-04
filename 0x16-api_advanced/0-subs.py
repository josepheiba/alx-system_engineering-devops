#!/usr/bin/python3
"""
0-subs.py
"""
import requests


def number_of_subscribers(subreddit):
    """
    0-subs.py
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
