from flask import Flask, jsonify
import instaloader

app = Flask(__name__)

@app.route("/")
def home():
    return "TEAMRAX0 API WORKING"

@app.route("/insta/<username>")
def insta(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        data = {
            "owner": "@TEAMRAX0",
            "username": profile.username,
            "followers": profile.followers,
            "following": profile.followees,
            "bio": profile.biography
        }

        return jsonify(data)

    except:
        return jsonify({"error": "user not found"})
