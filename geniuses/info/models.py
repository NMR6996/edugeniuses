from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
sinaqmodel = (
    ("asagisinif", "Aşağı siniflər"),
    ("blok9_10", "Blok 9 və 10-cu siniflər"),
    ("blok11", "Blok 11-ci sinif"),
    ("buraxilis9", "Buraxılış 9-cu sinif"),
    ("buraxilis10", "Buraxılış 10"),
    ("buraxilis11", "Buraxılış 11"),
)


class ExamCategory(models.Model):
    category_name = models.CharField(max_length=200, verbose_name="İmtahan kateqoriyası")
    is_active = models.BooleanField(default=False, verbose_name="Əsas səhifədə görünürlük")

    def __str__(self):
        return f'{self.category_name}'


class Exam(models.Model):
    category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE, verbose_name="Kateqoriya seç")
    exam_title = models.CharField(max_length=200, null=True, blank=True, verbose_name="Sınaq başlığı")
    exam_description = RichTextField(verbose_name="İmtahan haqqında", null=True, blank=True)
    exam_fee = models.IntegerField(verbose_name="İmtahan qiyməti")
    exam_date = models.DateField(verbose_name="İmtahan tarixi")
    exam_address = models.CharField(verbose_name="Sınaq keçiriləcək ünvan", null=True, blank=True, max_length=200)
    exam_img = models.ImageField(upload_to="exam/", null=True, blank=True, verbose_name="Reklam üçün şəkil")
    is_active = models.BooleanField(default=False, verbose_name="Əsas səhifədə görünürlük")

    def __str__(self):
        return f'{self.exam_date}'

    class Meta:
        ordering = ['-exam_date']


class ExamSubject(models.Model):
    exam_title = models.OneToOneField(Exam, on_delete=models.CASCADE, verbose_name="Sınaq seç")
    subject = RichTextField(verbose_name="Mövzu")

    def __str__(self):
        return f'{self.exam_title}'


class Sinaqlar(models.Model):
    sinaq_tarix = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="Sınaq adı")
    sinaq_nov = models.CharField(choices=sinaqmodel, max_length=100)
    sinaq_duzgun_cvb = models.TextField()
    sinaq_sagird_cvb = models.TextField()
    is_active = models.BooleanField(default=False)
    counter = models.IntegerField(default=0)

    letter_replacements = [('c', 'Ç'), ('e', 'Ə'), ('g', 'Ğ'), ('i', 'İ'), ('o', 'Ö'), ('s', "Ş"), ('u', 'Ü')]

    @staticmethod
    def replace_letters(input_str, replacements):
        for old_char, new_char in replacements:
            input_str = input_str.replace(old_char, new_char)
        return input_str

    def hesabla(self):
        sinaqs = Sinaqlar.objects.filter(is_active=True)
        for sinaq in sinaqs:
            if (sinaq.sinaq_nov == 'buraxilis10' and sinaq.counter == 0) or (sinaq.sinaq_nov == 'buraxilis11' and sinaq.counter == 0):
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb

                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    is_no = all_text[row_number][26:32]
                    sinif = all_text[row_number][33:34]
                    if sinif == 'a':
                        sinif = 10
                    elif sinif == 'b':
                        sinif = 11
                    f1_q = all_text[row_number][53:76]
                    f2_q = all_text[row_number][77:97]
                    f3_q = all_text[row_number][98:111]
                    f3_k_a = all_text[row_number][112:118] + all_text[row_number][119:125] + all_text[row_number][126:132] + all_text[row_number][133:139] + all_text[row_number][140:146]

                    d1_q = right_answer[0:23]
                    d2_q = right_answer[25:45]
                    d3_q = right_answer[47:60]
                    d3_k = right_answer[60:66] + right_answer[66:72] + right_answer[72:78] + right_answer[78:84] + right_answer[84:90]

                    if Buraxilis11.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = Buraxilis11.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.sinif = sinif
                        person.f1_q = f1_q
                        person.f2_q = f2_q
                        person.f3_q = f3_q
                        person.f3_k_a = f3_k_a
                        person.d1_q = d1_q
                        person.d2_q = d2_q
                        person.d3_q = d3_q
                        person.d3_k = d3_k
                        person.save()
                    else:
                        person = Buraxilis11.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, sinif=sinif, is_no=is_no,
                                                            f1_q=f1_q, f2_q=f2_q, f3_q=f3_q, f3_k_a=f3_k_a, d1_q=d1_q,
                                                            d2_q=d2_q, d3_q=d3_q, d3_k=d3_k)
                        person.save()
                else:
                    new_counter = 1
                    return new_counter
            elif sinaq.sinaq_nov == 'buraxilis9' and sinaq.counter == 0:
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb

                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    is_no = all_text[row_number][26:32]
                    sinif = all_text[row_number][33:34]

                    f1_q = all_text[row_number][53:79]
                    f2_q = all_text[row_number][80:106]
                    f3_q = all_text[row_number][107:120]
                    f3_k_a = all_text[row_number][121:127] + all_text[row_number][128:134] + all_text[row_number][135:141] + all_text[row_number][142:148] + \
                             all_text[row_number][149:155] + all_text[row_number][156:162] + all_text[row_number][163:169] + all_text[row_number][170:176]

                    d1_q = right_answer[0:26]
                    d2_q = right_answer[28:54]
                    d3_q = right_answer[56:69]
                    d3_k = right_answer[69:75] + right_answer[75:81] + right_answer[81:87] + right_answer[87:93] + \
                           right_answer[93:99] + right_answer[99:105] + right_answer[105:111] + right_answer[111:117]

                    if Buraxilis9.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = Buraxilis9.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.sinif = sinif
                        person.f1_q = f1_q
                        person.f2_q = f2_q
                        person.f3_q = f3_q
                        person.f3_k_a = f3_k_a
                        person.d1_q = d1_q
                        person.d2_q = d2_q
                        person.d3_q = d3_q
                        person.d3_k = d3_k
                        person.save()
                    else:
                        person = Buraxilis9.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, is_no=is_no, sinif=sinif,
                                                            f1_q=f1_q, f2_q=f2_q, f3_q=f3_q, f3_k_a=f3_k_a, d1_q=d1_q,
                                                            d2_q=d2_q, d3_q=d3_q, d3_k=d3_k)
                        person.save()
                else:
                    new_counter = 1
                    return new_counter

        return self.counter

    def save(self, *args, **kwargs):
        self.counter = self.hesabla()
        return super(Sinaqlar, self).save(*args, **kwargs)


class Buraxilis11(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    is_no = models.CharField(max_length=6)
    sinif = models.CharField(max_length=2)
    d1_q = models.CharField(max_length=23)  # -----------
    f1_q = models.CharField(max_length=23)
    f1_a4 = models.FloatField(default=0)
    f1_a5 = models.FloatField(default=0)
    f1_a6 = models.FloatField(default=0)
    f1_a27 = models.FloatField(default=0)
    f1_a28 = models.FloatField(default=0)
    f1_a29 = models.FloatField(default=0)
    f1_a30 = models.FloatField(default=0)
    d2_q = models.CharField(max_length=20)  # ----------------
    f2_q = models.CharField(max_length=20)
    f2_a46 = models.FloatField(default=0)
    f2_a47 = models.FloatField(default=0)
    f2_a48 = models.FloatField(default=0)
    f2_a49 = models.FloatField(default=0)
    f2_a50 = models.FloatField(default=0)
    f2_a56 = models.FloatField(default=0)
    f2_a57 = models.FloatField(default=0)
    f2_a58 = models.FloatField(default=0)
    f2_a59 = models.FloatField(default=0)
    f2_a60 = models.FloatField(default=0)
    d3_q = models.CharField(max_length=13)  # ---------------
    d3_k = models.CharField(max_length=30)
    f3_q = models.CharField(max_length=13)
    f3_k_a = models.CharField(max_length=34)
    f3_a79 = models.FloatField(default=0)
    f3_a80 = models.FloatField(default=0)
    f3_a81 = models.FloatField(default=0)
    f3_a82 = models.FloatField(default=0)
    f3_a83 = models.FloatField(default=0)
    f3_a84 = models.FloatField(default=0)
    f3_a85 = models.FloatField(default=0)
    cem = models.FloatField()

    def __str__(self):
        return f"{self.sinaq_no}"

    @property
    def f1_d_q(self):
        x = 0
        for number in range(23):
            if self.f1_q[number] == self.d1_q[number]:
                x += 1
        return x

    @property
    def f2_d_q(self):
        x = 0
        for number in range(20):
            if self.f2_q[number] == self.d2_q[number]:
                x += 1
        return x

    @property
    def f3_d_q(self):
        x = 0
        for number in range(13):
            if self.f3_q[number] == self.d3_q[number]:
                x += 1
        return x

    @property
    def f1_d_a(self):
        return round(sum([self.f1_a4, self.f1_a5, self.f1_a6, self.f1_a27, self.f1_a28, self.f1_a29, self.f1_a30]),
                     1) * 2

    @property
    def f2_d_a(self):
        return round(
            sum([self.f2_a46, self.f2_a47, self.f2_a48, self.f2_a49, self.f2_a50, self.f2_a56, self.f2_a57, self.f2_a58,
                 self.f2_a59, self.f2_a60]), 1) * 2

    @property
    def f3_d_a(self):
        return round(sum([self.f3_a79, self.f3_a80, self.f3_a81, self.f3_a82, self.f3_a83, self.f3_a84, self.f3_a85]),
                     1) * 2

    @property
    def f3_d_k(self):
        x = 0
        for i in range(0, 30, 6):
            if self.f3_k_a[i:i + 6] == self.d3_k[i:i + 6]:
                x += 1
        return x

    @property
    def f1_cem(self):
        return round(((100 * sum([self.f1_d_a, self.f1_d_q])) / 37), 2)

    @property
    def f2_cem(self):
        return round(((5 * sum([self.f2_d_a, self.f2_d_q])) / 2), 2)

    @property
    def f3_cem(self):
        return round((25 * sum([self.f3_d_a, self.f3_d_q, self.f3_d_k])) / 8, 2)

    def cem_func(self):
        return round(sum([self.f1_cem, self.f2_cem, self.f3_cem]), 2)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(Buraxilis11, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']


class Buraxilis9(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    is_no = models.CharField(max_length=6)
    sinif = models.CharField(max_length=2)
    d1_q = models.CharField(max_length=23)  # -----------
    f1_q = models.CharField(max_length=23)
    f1_a6 = models.FloatField(default=0)
    f1_a28 = models.FloatField(default=0)
    f1_a29 = models.FloatField(default=0)
    f1_a30 = models.FloatField(default=0)
    d2_q = models.CharField(max_length=20)  # ----------------
    f2_q = models.CharField(max_length=20)
    f2_a49 = models.FloatField(default=0)
    f2_a50 = models.FloatField(default=0)
    f2_a59 = models.FloatField(default=0)
    f2_a60 = models.FloatField(default=0)
    d3_q = models.CharField(max_length=13)  # ---------------
    d3_k = models.CharField(max_length=30)
    f3_q = models.CharField(max_length=13)
    f3_k_a = models.CharField(max_length=34)
    f3_a82 = models.FloatField(default=0)
    f3_a83 = models.FloatField(default=0)
    f3_a84 = models.FloatField(default=0)
    f3_a85 = models.FloatField(default=0)
    cem = models.FloatField()

    def __str__(self):
        return f"{self.sinaq_no}"

    @staticmethod
    def part_of_question(f_q, coordinate1):
        question_list = [f_q[:coordinate1], f_q[coordinate1:]]
        question_list[0] = question_list[0].replace(" ", "&nbsp;")
        question_list[1] = question_list[1].replace(" ", "&nbsp;")

        return question_list

    @property
    def f1_qq(self):
        return self.part_of_question(self.f1_q, 5)

    @property
    def f2_qq(self):
        return self.part_of_question(self.f2_q, 18)

    @property
    def f3_qq(self):
        return self.f3_q.replace(" ", "&nbsp;")

    @property
    def d1_qq(self):
        return self.part_of_question(self.d1_q, 5)

    @property
    def d2_qq(self):
        return self.part_of_question(self.d2_q, 18)

    @property
    def f1_d_q(self):
        x = 0
        for number in range(26):
            if self.f1_q[number] == self.d1_q[number]:
                x += 1
        return x

    @property
    def f2_d_q(self):
        x = 0
        for number in range(26):
            if self.f2_q[number] == self.d2_q[number]:
                x += 1
        return x

    @property
    def f3_d_q(self):
        x = 0
        for number in range(13):
            if self.f3_q[number] == self.d3_q[number]:
                x += 1
        return x

    @property
    def f1_d_a(self):
        return round(sum([self.f1_a6, self.f1_a28, self.f1_a29, self.f1_a30]), 1) * 2

    @property
    def f2_d_a(self):
        return round(
            sum([self.f2_a49, self.f2_a50, self.f2_a59, self.f2_a60]), 1) * 2

    @property
    def f3_d_a(self):
        return round(sum([self.f3_a82, self.f3_a83, self.f3_a84, self.f3_a85]), 1) * 2

    @property
    def f3_d_k(self):
        x = 0
        for i in range(0, 48, 6):
            if self.f3_k_a[i:i + 6] == self.d3_k[i:i + 6]:
                x += 1
        return x

    @property
    def f1_cem(self):
        return round(((100 * sum([self.f1_d_a, self.f1_d_q])) / 34), 2)

    @property
    def f2_cem(self):
        return round(((100 * sum([self.f2_d_a, self.f2_d_q])) / 34), 2)

    @property
    def f3_cem(self):
        return round((100 * sum([self.f3_d_a, self.f3_d_q, self.f3_d_k])) / 29, 2)

    def cem_func(self):
        return round(sum([self.f1_cem, self.f2_cem, self.f3_cem]), 2)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(Buraxilis9, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']
