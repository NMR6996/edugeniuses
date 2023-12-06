from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name=""),
    path('exams', views.exams, name="exams"),
    path('exams-details/<int:id>', views.exam_details, name="exams-details"),
    path('sinaqlar', views.sinaqs, name="sinaqlar"),
    path('sinaqcavab', views.sinaqcavab, name="sinaqcavab"),
    path('adminsinaqcavab', views.adminsinaqcavab, name="adminsinaqcavab")
]
