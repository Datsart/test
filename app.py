from flask import Flask, render_template, request, jsonify
import random
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.get_json()
    print(data)
    return jsonify({'data': data})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True) # для докера
    app.run(host='127.0.0.1', port=8000, debug=True)  # для python3 app.py
