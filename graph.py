from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Define
class Student(graphene.ObjectType):
    id = graphene.ID()
    name= graphene.String()
    age = graphene.Int()

# DummyData
SData = [{"id":"1","name":"xyz","age":"25"},{"id":"2","name":"abc","age":"26"}]
# Query Class
class Query(graphene.ObjectType):
    allStudent = graphene.List(Student)
    student = graphene.Field(Student,id=graphene.ID(required=True))

    def resolve_allStudent(root,info):
        return SData
    def resolve_student(root,info,id):
        return next ((s for s in SData if s['id']==id),None)    

#schema
schema = graphene.Schema(query=Query)
app = Flask(__name__)
app.add_url_rule("/graphql",view_func=GraphQLView.as_view("graphql",schema=schema,graphiql =True))

if __name__ =="__main__":
    app.run(debug=True)