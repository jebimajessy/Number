from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    def check_even_odd(num):
        return "Even" if num % 2 == 0 else "Odd"

    assert check_even_odd(2) == "Even"
    assert check_even_odd(7) == "Odd"
    assert check_even_odd(0) == "Even"
    assert check_even_odd(-3) == "Odd"

    return "All tests passed!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
