#!/usr/bin/python3
""" Advance API module """
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ Returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found
    for the given subreddit, the function return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Moh\'d Bello Ibrahim'}
    params = {
              "after": after,
              "count": count,
              "limit": 100
              }
    try:
        res = get(url, headers=header, params=params, allow_redirects=False)
        res.raise_for_status()

        results = res.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except Exception:
        return None


if __name__ == "__main__":
    print(len(recurse(argv[1])))
