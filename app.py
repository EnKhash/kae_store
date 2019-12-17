#all Khalid Maddah



from flask_mail import Mail, Message
import os

from flask import Flask, session, render_template, url_for, request, json

from waitress import serve


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'khaledmaddah1995@gmail.com'
app.config['MAIL_PASSWORD'] = 'remfzluosfocpopa'

mail = Mail(app)

#send email to user and company
@app.route('/', methods=['POST'])
def send_email():
    user_email = request.form['user_email']
    user_message = request.form['user_message']

    #send user message to company email
    usr_msg = Message('Customer - Contact Us', sender= f'{user_email}' , recipients= ['khaledmaddah1995@gmail.com'])
    usr_msg.body = f'''{user_message}'''
    mail.send(usr_msg)

    #reply confirmation to user
    msg = Message('We recieved your concerns', sender = 'noreply@KAEstore.com', recipients = [user_email])
    msg.body = f''' Hello { user_email }, we have recieved your email, we will get back to you in the next 48 hours'''
    mail.send(msg)
    return index()

#error 404 page
@app.errorhandler(404)
def error(error):
    return render_template('error.html', title='Error 404'), 404


#index page
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', items=popular_items(items)) 

#Registrarion page
@app.route('/registration')
def registration():
    return render_template('registration.html', title='Registration')

#about page
@app.route('/about')
def about():
    return render_template('about_us.html', title='About Us')

#contact page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

#load product.jsoon file
with open('./products.json') as f:
  items = json.load(f)


#sort items by boughtNum and store in popItems
popItems = sorted(items, key= lambda i: i['boughtNum'], reverse=True)

#item-discription page
@app.route('/item-description/<name>/<price>/<desc>/<path:img>/<rating>')
def itemDesc(name, price, desc, img, rating):
    return render_template('item-description.html', name=name, price=price, desc=desc, title=name, img=img, rating=rating)


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


if __name__ == '__main__':
#    print("-- DEBUG MODE ----")
#    app.run(debug=True, port='5091')

   print("--PRODUCTION MODE ---")
   p = os.environ.get('PORT')
   if p == '' or p == None:
       p = '5000'
   print(p)
   serve(app, host='0.0.0.0', port=p)
