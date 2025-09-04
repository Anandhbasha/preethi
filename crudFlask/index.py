# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask web application instance
app = Flask(__name__)

# A list to store student records (initial data with 2 students)
studentList = [
    {"id": 1, "name": "abc", "city": "Erode"},
    {"id": 2, "name": "xyz", "city": "CBE"}
]

# Define the route for the homepage ("/")
@app.route('/')
def index():
    # Render the index.html template and pass the studentList as 'student'
    return render_template("index.html", student=studentList)

# Variable to keep track of the next student ID
nextId = 3

# Route to add a new student, supports both GET and POST requests
@app.route('/addStu', methods=["GET", "POST"])
def add():
    global nextId  # Use global nextId so it can be updated
    if request.method == "POST":  # If the form is submitted
        name = request.form['name']   # Get the 'name' value from the form
        city = request.form['city']   # Get the 'city' value from the form
        # Append a new student dictionary to the studentList
        studentList.append({"id": nextId, "name": name, "city": city})
        nextId += 1  # Increment nextId for the next student
        return redirect(url_for("index"))  # Redirect back to homepage after adding
    # If request is GET, show the add.html form to user
    return render_template("add.html")

# Route to edit a student by their ID
@app.route('/edit/<int:stu_id>', methods=["GET", "POST"])
def edit(stu_id):
    # Find the student from studentList with matching ID, if not found returns None
    stud = next((s for s in studentList if s['id'] == stu_id), None)
    if not stud:  # If student not found, return error message
        return "Student is not found"
    if request.method == "POST":  # If form is submitted with updated details
        stud['name'] = request.form['name']  # Update the name
        stud['city'] = request.form['city']  # Update the city
        return redirect(url_for("index"))  # Redirect to homepage after update
    # If request is GET, show edit.html form with current student data
    return render_template('edit.html', stud=stud)

# Route to delete a student by ID
@app.route('/delete/<int:stu_id>')
def deleteInfo(stu_id):
    global studentList  # Use global studentList to modify it
    # Create a new list excluding the student with the given ID
    studentList = [s for s in studentList if s['id'] != stu_id]
    return redirect(url_for("index"))  # Redirect back to homepage after deletion

# Run the application only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask development server with debug mode ON
