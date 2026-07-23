from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Calculator Backend is Running"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    num1 = float(data["num1"])
    num2 = float(data["num2"])
    operation = data["operation"]

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"answer": "Cannot divide by zero"})
        result = num1 / num2
    else:
        return jsonify({"answer": "Invalid operation"})

    return jsonify({"answer": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)