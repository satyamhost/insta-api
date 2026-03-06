from flask import Flask, jsonify
import instaloader

app = Flask(__name__)

@app.route("/")
def home():
    return "TEAMRAX0 INSTAGRAM OSINT API"

@app.route("/insta/<username>")
def insta_info(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        posts = []
        count = 0

        for post in profile.get_posts():
            posts.append({
                "post_id": post.mediaid,
                "shortcode": post.shortcode,
                "caption": post.caption,
                "likes": post.likes,
                "comments": post.comments,
                "date": str(post.date),
                "is_video": post.is_video,
                "video_views": post.video_view_count,
                "url": post.url,
                "location": str(post.location)
            })

            count += 1
            if count == 10:  # last 10 posts
                break

        data = {
            "owner": "@TEAMRAX0",
            "username": profile.username,
            "userid": profile.userid,
            "full_name": profile.full_name,
            "biography": profile.biography,
            "external_url": profile.external_url,
            "followers": profile.followers,
            "following": profile.followees,
            "posts_count": profile.mediacount,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified,
            "profile_pic": profile.profile_pic_url,
            "business_category": profile.business_category_name,
            "igtv_videos": profile.igtvcount,
            "recent_posts": posts
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "owner": "@TEAMRAX0",
            "error": str(e)
        })
