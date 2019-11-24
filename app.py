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

#load product.json file
with open('products.json') as f:
  items = json.load(f)

#sort items by boughtNum and store in popItems
popItems = sorted(items, key= lambda i: i['boughtNum'], reverse=True)

#item-discription page
@app.route("/item-description/<int:item_index>")
def itemDesc(item_index):
    return render_template('item-description.html', presented_items= items[item_index], title=items[item_index]['name'])

#load product.json file
with open('products.json') as f:
  items = json.load(f)

app.run(debug= True)
