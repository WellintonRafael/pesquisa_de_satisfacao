from flask import Flask, render_template

app = Flask("pesquisa_de_satisfacao")

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
