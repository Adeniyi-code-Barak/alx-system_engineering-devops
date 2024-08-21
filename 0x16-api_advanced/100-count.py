#!/usr/bin/python3
"""
   Searches through a list of words and check,
   if they have appearance in Reddit hotlist
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """
       Takes a word_list and counts it's occurence in reddit,
       returning a dictionary, incase_sensitive
    """
    try:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        header = {"User-Agent": "Chrome"}
        params = {"limit": 100, "after": after}

        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()

        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            return None
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    count_dict[word] = count_dict.get(word, 0) + \
                            title.count(word.lower())

        next_page = data["data"]["after"]
        if next_page:
            return count_words(subreddit, word_list, after=next_page,
                               count_dict=count_dict)
        else:
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    except requests.exceptions.RequestException:
        return None
