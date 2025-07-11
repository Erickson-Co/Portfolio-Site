from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
                           name="Jack Erickson",
                           tagline="Aspiring Developer & Innovator",
                           projects=[
                               {"title": "Golf Tracker App", "description": "An application created to track my Golf scores and improvement"},
                               {"title": "Portfolio Website", "description": "A subpage to show my accomplishments and projects"},
                               {"title": "Blog CMS", "description": "A mini content management system."}
                           ])

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
