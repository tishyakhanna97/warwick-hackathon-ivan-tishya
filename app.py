from flask import Flask, render_template, request
from functions import combined

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    item = ""
    if request.method == "POST":
        item = request.form['item']
        results = combined(item)
    return render_template('index.html', results=results, item=item)


if __name__ == '__main__':
    app.run()
