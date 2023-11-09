from flask import Flask,render_template, url_for # used to access routes ie, for example for accessing css file from static directory.

app = Flask(__name__)
posts= [
    {'author':"raju",
     'tittle':"blogpost1",
     'content':"first post"
     },
     {
         'author':"revi",
         'tittle':"blogpost2",
         'content':"second Post"
     }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts= posts)

@app.route("/about")
def about():
    return render_template('about.html',title = "aboutPage")

@app.route("/register")
def register():
    return render_template('register.html',title = "Register Page")

@app.route("/login")
def login():
    return render_template('login.html',title = "Login Page")
if __name__== '__main__':
    app.run(debug = True)
