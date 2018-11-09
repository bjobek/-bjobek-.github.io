
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_list = ["check1","check2","check3","check4"]
    return render_template ("index.html", my_list = my_list)

@app.route("/meow")
def meow():
    return "MEOW."

if __name__ == "__main__":
    app.run(debug=True,host = "www.deltanet.no")
