from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", title="Home")

@app.get("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    # For local development only. In Azure, Gunicorn will be used automatically.
    app.run(host="0.0.0.0", port=8000, debug=True)

