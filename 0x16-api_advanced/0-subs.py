#!/usr/bin/python3
""" Advance API module """
from requests import get


def number_of_subscribers(subreddit):
    """ Get number of subscribers for a subreddit """
    headers = {'User-Agent': '0x16-api_advanced:project:\
    v1.0.0 (by /u/Moh\'d Bello Ibrahim'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=headers).json()
    try:
        return count.get('data', {}).get('subscribers', 0)
    except Exception:
        return 0
