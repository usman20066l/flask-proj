from flask import Flask, jsonify, render_template, request, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient("mongodb+srv://yuzen:Usman13%40@yuzen-perfumes.leixgxr.mongodb.net/?appName=YUZEN-Perfumes")
db = client["student_db"]
collection = db["students"]



# form page

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    try:
        
        name = request.form["name"]
        course = request.form["course"]

        data = {
            "name": name,
            "course": course
        }
        
        collection.insert_one(data)

        return redirect("/success")
    
    except Exception as e:

        return f"Error: {e}"
    
# Success Page

@app.route("/success")
def success():
    return render_template("success.html")

app.run(debug=True)