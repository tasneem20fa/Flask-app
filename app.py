# ...existing code...
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    port = int(os.getenv('PORT', '5000'))
    app.run(debug=debug, host='127.0.0.1', port=port)
# ...existing code...