from flask import Flask, session, render_template, url_for, request, json

app = Flask(__name__)

#error 404 page
@app.errorhandler(404)
def error(error):
    return render_template('error.html', title='Error 404'), 404

#index page
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home', items=popular_items(items), item_koko=items)

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
@app.route("/item-description/<name>/<price>/<desc>")
def itemDesc(name, price, desc):
    return render_template('item-description.html', name=name, price=price, desc=desc, title=name)


#item list page
@app.route('/item-list/<string:item_type>')
def item_list(item_type):
    return render_template('item-list.html', item_type=find_type(items, item_type), title=item_type + ' items')

def popular_items(items):
    for i in range(0,9):
        for j in range(i+1, len(items)):
            if items[i]['boughtNum'] < items[j]['boughtNum']:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
        yield items[i]
        json.dumps(items[i])
        

def find_type(items, itype):
    for i in range(0,len(items)):
        if(items[i]['type'] == 'PS4' and itype == "PS4"):
            yield items[i]
            json.dumps(items[i])
        elif(items[i]['type'] == 'Xbox' and itype == "Xbox"):
            yield items[i]
            json.dumps(items[i])
        elif(items[i]['type'] == 'PC' and itype == "PC"):
            yield items[i]
            json.dumps(items[i])



app.run(debug= True)
