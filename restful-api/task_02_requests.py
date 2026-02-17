#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        print([post['title'] for post in posts])
    else:
        return [] 
fetch_and_print_post()

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        structured_data = []
        for post in posts:
            structured_data.append({
                "id": post['id'],
                "title": post['title'],
                "body": post['body']
            })
        print(structured_data)
fetch_and_save_posts()
