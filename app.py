from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
                           name="Jack Erickson",
                           tagline="Aspiring Developer & Innovator",
                           projects=[
                               {"title": "Weather App", "description": "A weather dashboard using API data."},
                               {"title": "Portfolio Website", "description": "This very site!"},
                               {"title": "Blog CMS", "description": "A mini content management system."}
                           ])

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
