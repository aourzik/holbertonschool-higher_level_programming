#!/usr/bin/venv python3
"""Module that uses Jinja2 to generate HTML files from a template and a list of attendees"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
            return products
    except FileNotFoundError:
        return []

def read_json(filename):
    """Reads a JSON file and returns a list of dictionaries"""
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def read_sqlite(db_name):
    """Reads a SQLite database and returns a list of dictionaries"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3],
            })
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    """Route that displays a list of products from a CSV file or JSON file"""
    source = request.args.get('source')
    products_id = request.args.get('id')
    if source == 'csv':
        products_dict = read_csv('products.csv')
    elif source == 'json':
        products_dict = read_json('products.json')
    elif source == 'sql':
        products_dict = read_sqlite('products.db')
    else:
        return render_template('product_display.html',
                               error='Wrong source',
                               products=[])
    
    if products_id is not None:
        try:            
            products_id = int(products_id)
        except ValueError:
            return render_template('product_display.html',
                                   error='Invalid product ID',
                                   products=[])
    
        filtered_products = []
        for product in products_dict:
            if product.get('id') == products_id:
                filtered_products.append(product)
    
        if not filtered_products:
            return render_template('product_display.html',
                                error='Product not found',
                                products=[])
    
        return render_template('product_display.html', products=filtered_products)
    
    return render_template('product_display.html', products=products_dict) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)
