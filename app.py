from flask import Flask, request, jsonify
from youtubesearchpython import VideosSearch

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "running"}

@app.route("/api/yt/search")
def search():
    query = request.args.get("query")
    result = VideosSearch(query, limit=10).result()
    return jsonify(result)
