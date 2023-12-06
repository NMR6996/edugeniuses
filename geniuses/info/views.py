from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse

from .models import ExamCategory, Exam, ExamSubject, Sinaqlar, Buraxilis11, Buraxilis9


# Create your views here.

def index(request):
    categories = ExamCategory.objects.filter(is_active=True)[0:3]
    exams = Exam.objects.filter(is_active=True)

    return render(request, "index.html", {
        "categories": categories,
        "exams": exams
    })


def exams(request):
    exams = Exam.objects.filter(is_active=True)
    examspaginator = Paginator(exams, 6)
    page = request.GET.get('page')
    try:
        exams = examspaginator.page(page)
    except PageNotAnInteger:
        exams = examspaginator.page(1)
    except EmptyPage:
        exams = examspaginator.page(examspaginator.num_pages)
    return render(request, "exams.html", {"exams": exams})


def exam_details(request, id):
    exam = Exam.objects.get(id=id)
    subject = ExamSubject.objects.get(exam_title=exam)
    print()
    return render(request, "exam-details.html", {"exam": exam, "subject": subject})


def sinaqs(request):
    sinaqs = Sinaqlar.objects.all()
    return render(request, "sinaqs.html", {"sinaqs": sinaqs})


def adminsinaqcavab(request):
    id_input = request.GET.get('id')
    karne_input = request.GET.get('sinaqtipi')
    sinaq = Sinaqlar.objects.get(id=id_input)

    if sinaq.sinaq_nov == 'buraxilis10' or sinaq.sinaq_nov == 'buraxilis11':
        students = Buraxilis11.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "11buraxilis/karneumumi.html", {
                "students": students
            })
        elif karne_input == 'Siyahi':
            return render(request, "11buraxilis/list.html", {
                "students": students
            })
    elif sinaq.sinaq_nov == 'buraxilis9':
        students = Buraxilis9.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "9buraxilis/karneumumi.html", {
                "students": students
            })
        elif karne_input == 'Siyahi':
            return render(request, "9buraxilis/list.html", {
                "students": students
            })


def sinaqcavab(request):
    isno_input = request.GET.get('is_no')
    id_input = request.GET.get('id')
    sinaq = Sinaqlar.objects.get(id=id_input, is_active=True)

    if sinaq.sinaq_nov == 'buraxilis10' or sinaq.sinaq_nov == 'buraxilis11':
        try:
            students_ordered = Buraxilis11.objects.filter(sinaq_no=id_input).order_by('-cem')
            student = students_ordered.get(is_no=isno_input)

            student_index = list(students_ordered).index(student) + 1

            return render(request, "11buraxilis/ferdi.html", {"student": student, "student_index": student_index})

        except Buraxilis11.DoesNotExist:
            return HttpResponse('İş nömrəsi tapılmadı')

    elif sinaq.sinaq_nov == 'buraxilis9':
        try:
            students_ordered = Buraxilis9.objects.filter(sinaq_no=id_input).order_by('-cem')
            student = students_ordered.get(is_no=isno_input)

            student_index = list(students_ordered).index(student) + 1

            return render(request, "9buraxilis/ferdi.html", {"student": student, "student_index": student_index})

        except Buraxilis9.DoesNotExist:
            return HttpResponse('İş nömrəsi tapılmadı')
