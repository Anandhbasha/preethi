from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello welcome to flask"

if __name__=='__main__':
    app.run(debug=True)
