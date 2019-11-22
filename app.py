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
    for i in range(0,9):
        for j in range(i+1, len(items)):
            if items[i]['boughtNum'] < items[j]['boughtNum']:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
        return """
                <div class="col-lg-4 col-md-6 mb-4">
                <div class="card h-100">
                    <a href="#"><img class="card-img-top" src="/static/{{items[i]['img']}}" alt=""></a>
                    <div class="card-body">
                    <h4 class="card-title">
                        <a href="#">{{items[i]['name']}}</a>
                    </h4>
                    <h5>${{items[i]['price']}}</h5>
                    <p class="card-text">{{items[i]['description']}}</p>
                    </div>
                    <div class="card-footer">
                    <small class="text-muted">Rating: {{items[i]['rating']}}/5 ({{items[i]['boughtNum']}})</small>
                    </div>
                </div>
                </div>
            """



app.run(debug= True)
