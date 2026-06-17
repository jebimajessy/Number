from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    num = request.args.get("num")

    if num is None:
        return "Usage: /?num=10"

    try:
        num = int(num)
    except ValueError:
        return "Please provide a valid integer."

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
