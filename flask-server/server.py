from flask import Flask

app = Flask(__name__)

# Members API Route


@app.route("/members")
def members():
    return {"members": ["Member_1", "Member_2", "Member_3"]}


if __name__ == "__main__":
    app.run(debug=True)
