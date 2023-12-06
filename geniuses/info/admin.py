from django.contrib import admin
from .models import ExamCategory, Exam, ExamSubject, Sinaqlar, Buraxilis11, Buraxilis9

# Register your models here.


class AdminExamCategories(admin.ModelAdmin):
    list_display = ("category_name", "is_active")


class AdminExam(admin.ModelAdmin):
    list_display = ("exam_title", "exam_description", "exam_date", "exam_address", "is_active")


class AdminExamSubject(admin.ModelAdmin):
    list_display = ("exam_title",)


class AdminSinaqlar(admin.ModelAdmin):
    list_display = ("sinaq_tarix", "is_active", "counter")
    list_editable = ("is_active", "counter")
    search_fields = ("sinaq_adi",)


class AdminBuraxilis11(admin.ModelAdmin):
    list_display = ("sinaq_no", "aad", "soyad", "sinif", "f1_a4", "f1_a5", "f1_a6", "f1_a27", "f1_a28", "f1_a29", "f1_a30", "f2_a46", "f2_a47", "f2_a48", "f2_a49", "f2_a50", "f2_a56", "f2_a57", "f2_a58", "f2_a59", "f2_a60", "f3_a79", "f3_a80", "f3_a81", "f3_a82", "f3_a83", "f3_a84", "f3_a85", "cem")
    list_editable = ("f1_a4", "f1_a5", "f1_a6", "f1_a27", "f1_a28", "f1_a29", "f1_a30", "f2_a46", "f2_a47", "f2_a48", "f2_a49", "f2_a50", "f2_a56", "f2_a57", "f2_a58", "f2_a59", "f2_a60", "f3_a79", "f3_a80", "f3_a81", "f3_a82", "f3_a83", "f3_a84", "f3_a85")
    list_filter = ("sinaq_no", "aad", "soyad", "sinif")


class AdminBuraxilis9(admin.ModelAdmin):
    list_display = ("sinaq_no", "aad", "soyad", "sinif", "f1_a6", "f1_a28", "f1_a29", "f1_a30", "f2_a49", "f2_a50", "f2_a59", "f2_a60", "f3_a82", "f3_a83", "f3_a84", "f3_a85", "cem")
    list_editable = ("f1_a6", "f1_a28", "f1_a29", "f1_a30", "f2_a49", "f2_a50", "f2_a59", "f2_a60", "f3_a82", "f3_a83", "f3_a84", "f3_a85")
    list_filter = ("sinaq_no", "aad", "soyad", "sinif")


admin.site.register(ExamCategory, AdminExamCategories)
admin.site.register(Exam, AdminExam)
admin.site.register(ExamSubject, AdminExamSubject)
admin.site.register(Sinaqlar, AdminSinaqlar)
admin.site.register(Buraxilis11, AdminBuraxilis11)
admin.site.register(Buraxilis9, AdminBuraxilis9)
