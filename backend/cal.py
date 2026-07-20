from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.json

    num1 = int(data["num1"])
    num2 = int(data["num2"])

    return jsonify({
        "answer": num1 + num2
    })

if __name__ == "__main__":
    app.run()