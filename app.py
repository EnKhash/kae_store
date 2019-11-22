from flask import Flask, session, render_template, url_for, request, json

app = Flask(__name__)


#index page
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

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



def products(items):
    for i in range(9):
        for j in range(i+1):
            if items[i]['boughtNum'] > items[j]['boughtNum']:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
        print(i)

#loop through products in products.json
def koko():
    for i in items:
        products(i)
        print (i['name'])

products(items['name'])

app.run(debug= True)
