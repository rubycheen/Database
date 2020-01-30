from django.shortcuts import render
from django.http import HttpResponse
from students.models import Students, Response, Assist, Course, CourseProperties, Feedback, Professor, Score, Student, TA, Take, Teach
import csv

# Create your views here.


def students_list(request):
    return render(request, 'initial.html')


def echo(request):
    data = request.POST['num']
    return render(request, 'result.html', {'data': data})


def get_by_grade(request):
    g = request.POST['grade']
    data = Response.objects.filter(Grade=g)
    return render(request, 'initial.html', {'data': data})


def get_csv(request):
    path = '/Users/sevenstars/Downloads/dbms.csv'
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Response.objects.create(StudentNumber=row['StudentNumber'], StudentName=row['StudentName'], College=row['College'], Department=row['Department'], Grade=row['Grade'], Gender=row['Gender'], CourseNumber=row['CourseNumber'], Year=row['Year'], CourseName=row['CourseName'], Category=row['Category'], Credit=row['Credit'], Professor=row['ProfessorName'], ProfessorNumber=row['ProfessorNumber'], TAName=row['TAName'], TANumber=row['TANumber'], RollCall=row['RollCall'], Attendance=row['Attendance'], SweetScore=row['SweetScore'], FreeScore=row['FreeScore'], AcquisitionScore=row['AcquisitionScore'], CourseGrade=row['CourseGrade'], Recommendation=row['Recommendation'])

    return render(request, 'initial.html', {'number': "OK"})


def retrieve_data(request):
    if "CourseName" in request.POST:
        cn = request.POST["CourseName"]
        data1 = Response.objects.filter(CourseName=cn)
        data2 = Response.objects.filter(pk=-10)
        data3 = Response.objects.filter(pk=-10)
        space = "                    "
        return render(request, "initial.html", {"datas1": data1, "datas2": data2, "datas3": data3, "space": space})
    elif "CourseNumber" in request.POST:
        cn = request.POST["CourseNumber"]
        data1 = Response.objects.filter(pk=-10)
        data2 = Response.objects.filter(CourseNumber=cn)
        data3 = Response.objects.filter(pk=-10)
        space = "                    "
        return render(request, "initial.html", {"datas1": data1, "datas2": data2, "datas3": data3, "space": space})
    elif "Professor" in request.POST:
        cn = request.POST["Professor"]
        data1 = Response.objects.filter(pk=-10)
        data2 = Response.objects.filter(pk=-10)
        data3 = Response.objects.filter(Professor=cn)
        space = "                    "
        return render(request, "initial.html", {"datas1": data1, "datas2": data2, "datas3": data3, "space": space})
    else:
        data = Response.objects.all()
    return render(request , "initial.html" , {"datas":data})


def import_data_assist(request):
    path = "/Users/翊毛/Desktop/aaaa/assist.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Assist.objects.create(TANumber = row["TANumber"], CourseNumber = row["CourseNumber"])

    return render(request, 'initial.html', {'number': "OK"})


def import_data_course(request):
    path = "/Users/翊毛/Desktop/aaaa/course.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Course.objects.create(CourseNumber=row["CourseNumber"], CourseName=row["CourseName"], Category=row["Category"], Credit=row["Credit"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_courseproperties(request):
    path = "/Users/翊毛/Desktop/aaaa/CourseProperty.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            CourseProperties.objects.create(CourseNumber=row["CourseNumber"], SweetScore=row["SweetScore"], FreeScore=row["FreeScore"], RollCall=row["RollCall"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_feedback(request):
    path = "/Users/翊毛/Desktop/aaaa/feedback.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Feedback.objects.create(CourseNumber=row["CourseNumber"], AcquisitionScore=row["AcquisitionScore"], Recommendation=row["Recommendation"], StudentName=row["StudentName"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_professor(request):
    path = "/Users/翊毛/Desktop/aaaa/professor.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Professor.objects.create(ProfessorNumber=row["ProfessorNumber"], TAName=row["TAName"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_score(request):
    path = "/Users/翊毛/Desktop/aaaa/score.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Score.objects.create(CourseNumber=row["CourseNumber"], CourseGrade=row["CourseGrade"], StudentNumber=row["StudentNumber"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_student(request):
    path = "/Users/翊毛/Desktop/aaaa/student.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Student.objects.create(StudentNumber=row["StudentNumber"], StudentName=row["StudentName"], Gender=row["Gender"], Grade=row["Grade"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_TA(request):
    path = "/Users/翊毛/Desktop/aaaa/TA.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            TA.objects.create(TANumber=row["TANumber"], TAName=row["TAName"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_take(request):
    path = "/Users/翊毛/Desktop/aaaa/take.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Take.objects.create(StudentNumber=row["StudentNumber"], CourseNumber=row["CourseNumber"])

    return render(request, 'initial.html', {'number': "OK"})

def import_data_teach(request):
    path = "/Users/翊毛/Desktop/aaaa/teach.csv"
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            Teach.objects.create(ProfessorNumber=row["ProfessorNumber"], CourseName=row["CourseName"])

    return render(request, 'initial.html', {'number': "OK"})