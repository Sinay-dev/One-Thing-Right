from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '5aa97e5e0fb05044543228ad1d898ae9'


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
    

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title=Inscription, form=form )


@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Vous êtes connecté', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title=Login, form=form )


if __name__ == '__main__':
    app.run(debug=True)

