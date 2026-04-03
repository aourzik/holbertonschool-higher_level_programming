#!/usr/bin/venv python3
"""Module that uses Jinja2 to generate HTML files from a template and a list of attendees"""
from flask import Flask, render_template
import json
import csv

app = Flask(__name__)

def read_csv(filename):
    """Reads a CSV file and returns a list of dictionaries"""
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            products = []
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price']),
                })
    except FileNotFoundError:
        return []

def read_json(filename):
    """Reads a JSON file and returns a list of dictionaries"""
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/products')
def products():
    """Route that displays a list of products from a CSV file or JSON file"""
    products = read_csv('products.csv') or read_json('products.json')
    return render_template('products.html', products=products.get('products', []))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
