from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login16", methods=["GET", "POST"])
def login16():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        return render_template(
            "result16.html",
            username=username,
            password=password
        )

    return render_template("index16.html")


if __name__ == "__main__":
    app.run(debug=True)
