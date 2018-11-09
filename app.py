
from flask import Flask, render_template

app = FLask(__name__)

@app.route('/')
def index():
    my_list = ["apples","oranges","grapes","pineapples"]
    return render_template ("index.html",my_list = my_list)

@app.route("/meow")
def meow():
    return "MEOW."

if __name__ == "__main__":
    app.run(debug=True,host = "0.0.0.0")
