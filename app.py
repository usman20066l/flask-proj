from flask import Flask, jsonify, render_template, request, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient("mongodb+srv://yuzen:Usman13%40@yuzen-perfumes.leixgxr.mongodb.net/?appName=YUZEN-Perfumes")
db = client["todo_db"]
collection = db["todos"]



# form page

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    collection.insert_one({
        "itemName" : itemName,
        "itemDescription": itemDescription
    })

    return "data stored successfully"
  

    
# Success Page

@app.route("/success")
def success():
    return render_template("success.html")

app.run(debug=True)