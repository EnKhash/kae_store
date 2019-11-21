from flask import Flask, session, render_template, url_for, request, json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route("/registration")
def registration():
    return render_template('registration.html', title='Registration')

@app.route("/about")
def about():
    return render_template('about_us.html', title='About Us')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Us')



with open('kae_store/products.json') as f:
  data = json.load(f)


app.run(debug= True)
