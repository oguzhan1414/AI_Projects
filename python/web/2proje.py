from flask import Flask , render_template

app = Flask(__name__)

posts = [
    {"id":1,"title":"Introduction to flask","content":"Flask Öğrenmek için yol haritası:"},
    {"id":2,"title":"Bazı özel durumlar 2","content":"Bazı özel durumları öğrenmek"}
]

@app.route('/')
def home():
    return render_template('index2.html',posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post= next((post for post in posts if post["id"] == post_id),None)
    if post:
        return render_template('post.html',post=post)
    return "<h1> Post Not Found </h1>",404

if __name__ == '__main__':
    app.run(debug=True)