# from flask import Flask,render_template
#
# app = Flask(__name__)
# @app.route('/')
# def index():
#     try:
#         f = open('Scores.txt', 'r')
#         g = f.read()
#     except:
#         return open("Errorhtml.html")
#     return render_template('index.html',n=g)
#
# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask, render_template
import ast  # Import the ast module for safely evaluating literal expressions

app = Flask(__name__)

def get_scores():
    try:
        with open('Scores.txt', 'r') as f:
            content = f.read()
            if content:
                scores = ast.literal_eval(content)  # Safely evaluate the literal expression
            else:
                scores = {}
    except FileNotFoundError:
        scores = {}
    return scores

@app.route('/')
def index():
    scores = get_scores()
    return render_template('index.html', n=scores)  # Pass the 'scores' dictionary to the template

if __name__ == "__main__":
    app.run(debug=True)
