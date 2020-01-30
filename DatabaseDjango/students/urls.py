"""db_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('echo', views.echo, name='echo'),
    path('get_by_grade', views.get_by_grade, name='get_by_grade'),
    path('get_csv', views.get_csv, name='get_csv'),
    path('retrieve_data', views.retrieve_data, name='retrieve_data'),
    path('import_data_assist', views.import_data_assist, name='import_data_assist'),
    path('import_data_course', views.import_data_course, name='import_data_course'),
    path('import_data_courseproperties', views.import_data_courseproperties, name='import_data_courseproperties'),
    path('import_data_feedback', views.import_data_feedback, name='import_data_feedback'),
    path('import_data_professor', views.import_data_professor, name='import_data_professor'),
    path('import_data_score', views.import_data_score, name='import_data_scorer'),
    path('import_data_student', views.import_data_student, name='import_data_student'),
    path('import_data_TA', views.import_data_TA, name='import_data_TA'),
    path('import_data_take', views.import_data_take, name='import_data_take'),
    path('import_data_teach', views.import_data_teach, name='import_data_teach'),
]
