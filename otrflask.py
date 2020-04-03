from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/liste")
def liste():
    return render_template('liste.html', title="Liste")

@app.route("/inv")
def inventaire():
    return render_template('inventaire.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)
