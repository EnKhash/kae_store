from flask import Flask, session, render_template, url_for, request, json

app = Flask(__name__)


#index page
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home' , items=popItems)

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
with open('kae_store/products.json') as f:
  items = json.load(f)

#sort items by boughtNum and store in popItems
popItems = sorted(items, key= lambda i: i['boughtNum'], reverse=True)


#write popItems to popular-products.json
with open('kae_store/popular-products.json', 'w') as p:
    json.dump(popItems, p)




app.run(debug= True)
