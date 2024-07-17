from flask import Flask, render_template
from markupsafe import escape
import requests


app = Flask(__name__)


@app.route('/blog')
def blog():
    response = requests.get("https://api.npoint.io/db68389ed6d1c2241a59")
    data = response.json()
    return render_template("blog.html", posts=data)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/guess/<name>')
def guess(name):
    # agify
    url1 = f"https://api.agify.io?name={escape(name)}"
    response1 = requests.get(url=url1)
    data1 = response1.json()
    url2 = f"https://api.genderize.io?name={escape(name)}&country_id=BR"
    response2 = requests.get(url=url2)
    data2 = response2.json()
    # return data2
    return render_template("index.html", name=data1["name"], age=data1["age"], gender=data2["gender"])


if __name__ == "__main__":
    app.run(debug=True)

# model
# """[
#   {
#   "id": 1,
#   "title": "first one",
#   "text": "Lorem ipsum dolot sit amet1"
# },
# {
#   "id": 2,
#   "title": "second one",
#   "text": "Lorem ipsum dolot sit amet2"
# },
# {
#   "id": 3,
#   "title": "third one",
#   "text": "Lorem ipsum dolot sit amet3"
# }
# ]"""