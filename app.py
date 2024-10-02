from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
