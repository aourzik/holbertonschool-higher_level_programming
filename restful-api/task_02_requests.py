#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        return [] 
fetch_and_print_posts()

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
    
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            final_file = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            final_file.writeheader()
            final_file.writerows(structured_data)
fetch_and_save_posts()
