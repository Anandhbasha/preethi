from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

studentList = [
    {"id":1,"name":"abc","city":"Erode"},{"id":2,"name":"xyz","city":"CBE"}
]

@app.route('/')
def index():
    return render_template("index.html",student =studentList)

nextId = 3

@app.route('/addStu',methods = ["GET","POST"])
def add():
    global nextId
    if request.method == "POST":
        name = request.form['name']
        city = request.form['city']
        studentList.append({"id":nextId,"name":name,"city":city})
        nextId+=1
        return redirect(url_for("index"))
    return render_template("add.html")

# @app.route('/edit/<int:stu_id>',methods=["GET","POST"])
# def edit(stu_id):
#     stud = next((s for s in studentList if s['id']==stu_id),None)
#     if not stud:
#         return "Student is not found"
#     if request.method=="POST":
#         stud['name'] = request.form['name']
#         stud['city'] = request.form['city']
#         return redirect(url_for("index"))
#     return render_template('edit.html',stud = stud)

if __name__ == '__main__':
    app.run(debug=True)