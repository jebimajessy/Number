from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Even or Odd Checker</title>
</head>
<body>
    <h2>Even or Odd Checker</h2>

    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="num" required>
        <button type="submit">Check</button>
    </form>

    {% if result %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        num = int(request.form["num"])

        if num % 2 == 0:
            result = "Even"
        else:
            result = "Odd"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
