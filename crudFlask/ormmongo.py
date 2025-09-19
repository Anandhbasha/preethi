import mongoengine as me

me.connect("studentList")

class StudentNames(me.Document):
    name=me.StringField(required=True)
    rollNo= me.StringField(required=True)
    city=me.StringField(required=True)
    ContactNo=me.IntField(required=True)

addStud = StudentNames(name="rahul",rollNo="111AE002",city="Trichy",ContactNo=97845545454)
addStud.save()

for s in StudentNames.objects:
    print(s.name)