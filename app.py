from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# Replace with your MongoDB Atlas connection string
client = MongoClient("mongodb+srv://pushpendumukherjee9:i4gENvIP1lvfBhs1@cluster0.gcmytqo.mongodb.net/flaskdb?retryWrites=true&w=majority")
db = client["flaskdb"]
collection = db["userdata"]

@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        collection.insert_one({'name': name, 'email': email})
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
