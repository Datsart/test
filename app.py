from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def func():
    data = request.get_json()
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
