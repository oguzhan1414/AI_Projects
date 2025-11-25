from flask import Flask,render_template

#Create Flask App
app = Flask(__name__)

#Route tanımlıcaz
@app.route('/')
def home():
    return render_template('index.html')

#farklı bir rota
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html',name=name)

#oturum çalıştırma
if __name__ == '__main__':
    app.run(debug=True)