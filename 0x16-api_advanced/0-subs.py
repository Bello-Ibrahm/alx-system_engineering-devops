#!/usr/bin/python3
""" Advance API module """
from requests import get


def number_of_subscribers(subreddit):
    """ Get number of subscribers for a subreddit """
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers={'User-Agent': 'Moh\'d Bello Ibrahim'}).json()
    try:
        return count.get('data', {}).get('subscribers', 0)
    except Exception:
        return (0)
