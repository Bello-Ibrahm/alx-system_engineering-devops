#!/usr/bin/python3
""" Advance API module """
from requests import get


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
    for a given subreddit. """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(
        subreddit)
    header = {
            'User-Agent': 'Moh\'d Bello Ibrahim'
            }
    param = {
            'limit': 10
            }
    try:
        req = get(url, headers=header, params=param, allow_redirects=False).json()
        res = req.get('data').get('children')
        print('\n'.join([dic.get('data').get('title')
                         for dic in res]))
    except Exception:
        print('None')
