#!/usr/bin/python3
"""Module that prints title of hot subbreddit"""

import requests


def top_ten(subreddit):
    """Takes in a subreddit and prints the top hot"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    header = {'User-agent': 'Chrome'}
    try:
        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()

        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print("None")
        else:
            for post in posts:
                title = post["data"]["title"]
                print(title)

    except requests.exceptions.RequestException:
        print("None")
