#!/usr/bin/python3
""" Advance API module """
from requests import get


def number_of_subscribers(subreddit):
    """ Get number of subscribers for a subreddit """
    header = {
            'User-Agent': 'Moh\'d Bello Ibrahim'
            }
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=header).json()
    try:
        return count.get('data').get('subscribers')
    except Exception:
        return 0
