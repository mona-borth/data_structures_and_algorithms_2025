from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', heading = 'My personal home page')

@app.route("/hello")
@app.route("/hello/<city>")
def hello(city=None):
    if city is None:
        return "<h1>Hello there!</h1>"
    else:
        return f"<h1>Hello, {city}!</h1>"
    
@app.route("/about")
def about():
    return render_template('about.html', heading = 'My About Page')

if __name__ == '__main__':
    app.run(debug=True)