#!/usr/bin/python3
""" Advance API module """
from requests import get


def number_of_subscribers(subreddit):
    """ Get number of subscribers for a subreddit """
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {'User-Agent': '0x16-api_advanced:project:\
    v1.0.0 (by /u/Moh\'d Bello Ibrahim'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=headers).json()
    return count.get('data', {}).get('subscribers', 0)
