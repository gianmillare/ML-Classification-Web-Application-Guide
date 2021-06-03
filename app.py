from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from requests.api import request
import os

app = Flask(__name__)
Bootstrap(app)

"""Routes"""
@app.route('/', methods=['GET'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)