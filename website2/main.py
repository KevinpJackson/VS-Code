from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

from website2 import create_app

app = create_app()

if __name__== "__main__":
    app.run(debug=True)