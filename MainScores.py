from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    try:
        f = open('Score.txt', 'r')
        g = f.read()
    except:
        return open("Errorhtml.html")
    return render_template('index.html',n=g)

if __name__=="__main__":
    app.run(debug=True)