#!/usr/bin/env python3

import requests

def fetch_and_print_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        print([post['title'] for post in posts])
    else:
        return [] 
fetch_and_print_post()
