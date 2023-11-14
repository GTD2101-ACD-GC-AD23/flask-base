from flask import Flask
from traducir import traducirEn2Es

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"

@app.route("/<nombre>")
def hola(nombre):
    return f"Hola {nombre}"

@app.route("/traducir/<text>")
def traducir(text):
    print(text)
    return traducirEn2Es(text)

@app.route('/about')
def about():
    return "<h1>Acerca de</h1><br><p>Este grupo es asombroso</p>"
    #pass
    #return render_template('about.html', title='about', name='Passed by variable')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)