from marshmallow import Schema, fields, post_load
from .models import Student, Course, Teacher


class StudentSchema(Schema):
    first_name = fields.Str(required=True)
    second_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    create_time = fields.Str(required=True)

    @post_load
    def make_student(self, data, **kwargs):
        return Student(**data)


class TeacherSchema(Schema):
    first_name = fields.Str(required=True)
    second_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    create_time = fields.Str(required=True)

    @post_load
    def make_teacher(self, data, **kwargs):
        return Teacher(**data)


class CourseSchema(Schema):
    name = fields.Str(required=True)
    credits = fields.Int(required=True)
    url = fields.Str(required=True)
    teacher_id = fields.Int(required=True)

    @post_load
    def make_course(self, data, **kwargs):
        return Course(**data)



class JoinRequest(Schema):
    create_time = fields.Str(required=True)
    student_id =fields.Int(required=True)
    course_id =fields.Int(required=True)
    status = fields.Str(validate=lambda x: x in ['accepted', 'denied', 'unprocessed'], required=True)




