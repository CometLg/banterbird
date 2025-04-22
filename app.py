from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/posts')
def get_posts():
    with (open("data.json", "r")) as file:
        posts = json.load(file)
    return jsonify(posts)

@app.route('/api/add_post', methods=['POST'])
def add_post():
    new_post = request.get_json()
    
    with (open("data.json", "r")) as file:  # open data.json file as read
        posts = json.load(file)  # loads data.json file
    posts.insert(0, new_post) # add the post to the top of the file
    
    with (open("data.json", "w")) as file:  # open data.json file as write
        json.dump(posts, file, indent=4) # dumps the posts into the data file
    
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True)
