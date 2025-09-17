import cherrypy

# class Helloworld:
#     @cherrypy.expose
#     def index(self):
#         return "Hello world"
    
# if __name__ == "__main__":
#     cherrypy.quickstart(Helloworld())

todo =[]

students = []

class StudentApi:
    @cherrypy.expose
    def index(self):
        return "Welcome to Crud"
    
    @cherrypy.expose
    def create(self,name,age):
        student = {'id':len(students)+1,"name":name,"age":age}
        students.append(student)
        return f'Student Added :{student}'
    @cherrypy.expose
    def read(self):
        return str(students)
    @cherrypy.expose
    def update(self,id,name=None,age=None):
        id = int(id)
        for s in students:
            if s['id']==id:
                if name:
                    s['name'] = name
                if age:
                    s['age']=age
                return f'updates:{s}'
            return "student not found"
        
if __name__ == "__main__":
    cherrypy.quickstart(StudentApi())