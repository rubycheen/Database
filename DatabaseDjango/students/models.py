from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.TextField(default="沒名字")
    area = models.TextField(default="北區")
    grade = models.TextField(default="一年級")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "students_list"

class Response(models.Model):
    StudentNumber =  models.TextField(default="B00000000")
    StudentName = models.TextField(default="哈哈哈")
    College = models.TextField(default="管理學院")
    Department = models.TextField(default="資訊管理系")
    Grade = models.TextField(default="一")
    Gender = models.TextField(default="生理男")
    CourseNumber = models.TextField(default="IM2002")
    Year = models.TextField(default="100")
    CourseName = models.TextField(default="管理學")
    Category = models.TextField(default="必修")
    Credit = models.TextField(default="3")
    Professor = models.TextField(default="謝冠雄")
    ProfessorNumber = models.TextField(default="T00001")
    TAName = models.TextField(default="你是誰")
    TANumber = models.TextField(default="TA000")
    RollCall = models.TextField(default="不點名")
    Attendance = models.TextField(default="0")
    SweetScore = models.TextField(default="0")
    FreeScore = models.TextField(default="0")
    AcquisitionScore = models.TextField(default='0')
    CourseGrade = models.TextField(default="A")
    Recommendation = models.TextField(default="0")

    class Meta:
        db_table = "response"


class Assist(models.Model):
    TANumber = models.TextField(default="TA000")
    CourseNumber = models.TextField(default="IM2002")

    class Meta:
        db_table = "assist"

class Course(models.Model):
    CourseNumber = models.TextField(default="IM2002")
    CourseName = models.TextField(default="管理學")
    Category = models.TextField(default="必修")
    Credit = models.TextField(default="3")

    class Meta:
        db_table = "course"

class CourseProperties(models.Model):
    CourseNumber = models.TextField(default="IM2002")
    SweetScore = models.TextField(default="0")
    FreeScore = models.TextField(default="0")
    RollCall = models.TextField(default="不點名")

    class Meta:
        db_table = "courseproperties"

class Feedback(models.Model):
    CourseNumber = models.TextField(default="IM2002")
    AcquisitionScore = models.TextField(default="0")
    Recommendation = models.TextField(default="0")
    StudentName = models.TextField(default="哈哈哈")

    class Meta:
        db_table = "feedback"

class Professor(models.Model):
    ProfessorNumber = models.TextField(default="T00001")
    TAName = models.TextField(default="你是誰")

    class Meta:
        db_table = "professor"

class Score(models.Model):
    CourseNumber = models.TextField(default="IM2002")
    CourseGrade = models.TextField(default="A")
    StudentNumber = models.TextField(default="B00000000")

    class Meta:
        db_table = "score"

class Student(models.Model):
    StudentNumber = models.TextField(default="B00000000")
    StudentName = models.TextField(default="哈哈哈")
    Gender = models.TextField(default="生理男")
    Grade = models.TextField(default="一")

    class Meta:
        db_table = "student"

class TA(models.Model):
    TANumber = models.TextField(default="TA000")
    TAName = models.TextField(default="你是誰")

    class Meta:
        db_table = "TA"

class Take(models.Model):
    StudentNumber = models.TextField(default="B00000000")
    CourseNumber = models.TextField(default="IM2002")

    class Meta:
        db_table = "take"

class Teach(models.Model):
    ProfessorNumber = models.TextField(default="T00001")
    CourseName = models.TextField(default="管理學")

    class Meta:
        db_table = "teach"