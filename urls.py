from django.urls import path
from fapp.views import addadmission
from fapp.views import admissionreport
from fapp.views import delstudent
from fapp.views import updatestudent
from fapp.views import Teacherread
from fapp.views import Teacherdetail
from fapp.views import Insertteacher
from fapp.views import Updateteacher
from django.contrib.auth.decorators import login_required
from fapp.views import logoutuser
from django.contrib import admin
from django.urls import path
from fapp import views



urlpatterns = [
    path('f1/', addadmission),
    path('port/', admissionreport),
    path ('delete/<int:id>',delstudent),
    path ('update/<int:id>',updatestudent),
    path ('teachl/',Teacherread.as_view(),name='listteacher'),
    path ('tede/<int:pk>',Teacherdetail.as_view()),
    path ('tinsert/',Insertteacher.as_view()),
    path('tede.<int:pk>/',Teacherdetail.as_view(),name='listteacher'),
    path ('uptech/<int:pk>/',Updateteacher.as_view()),
    path('getteacherdetail/<int:pk>/',login_required(Teacherdetail.as_view())),
    path('useout/',logoutuser),
    path('admin/',  admin.site.urls),
    path('setcookie/',views.setcookie),
    path('getcookie/',views.getcookie),
    path('setsession/',views.setsession),
    path('getsession/',views.getsession),
    path('getfile/',views.getfile),
    path('getpdf/',views.getpdf),
]
