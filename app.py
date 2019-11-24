from flask import Flask, session, render_template, url_for, request, json

app = Flask(__name__)


#index page
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home' , items=sorted(items, key= lambda i: i['boughtNum'], reverse=True))

#Registrarion page
@app.route("/registration")
def registration():
    return render_template('registration.html', title='Registration')

#about page
@app.route("/about")
def about():
    return render_template('about_us.html', title='About Us')

#contact page
@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Us')

#item-discription page
@app.route("/item-description/<string:name>/<float:price>/<string:desc>/<string:img>")
def itemDesc(name, price, desc, img):
    return render_template('item-description.html', name=name, title=name, price=price, desc=desc, img=img)


#load product.json file
with open('products.json') as f:
  items = json.load(f)

app.run(debug= True)
