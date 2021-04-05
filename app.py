from flask import Flask, render_template

from controllers.shop_controller import guitar_blueprint

app = Flask(__name__)

app.register_blueprint(guitar_blueprint)

@app.route('/')
def home_page():
    return render_template("home.html", title = "Home")

if __name__ == '__main__':
    app.run(debug=True)