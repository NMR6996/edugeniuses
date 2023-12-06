# Generated by Django 4.2.7 on 2023-12-05 07:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buraxilis11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinaq_no', models.CharField(max_length=100)),
                ('aad', models.CharField(max_length=12)),
                ('soyad', models.CharField(max_length=12)),
                ('is_no', models.CharField(max_length=6)),
                ('sinif', models.CharField(max_length=2)),
                ('d1_q', models.CharField(max_length=23)),
                ('f1_q', models.CharField(max_length=23)),
                ('f1_a4', models.FloatField(default=0)),
                ('f1_a5', models.FloatField(default=0)),
                ('f1_a6', models.FloatField(default=0)),
                ('f1_a27', models.FloatField(default=0)),
                ('f1_a28', models.FloatField(default=0)),
                ('f1_a29', models.FloatField(default=0)),
                ('f1_a30', models.FloatField(default=0)),
                ('d2_q', models.CharField(max_length=20)),
                ('f2_q', models.CharField(max_length=20)),
                ('f2_a46', models.FloatField(default=0)),
                ('f2_a47', models.FloatField(default=0)),
                ('f2_a48', models.FloatField(default=0)),
                ('f2_a49', models.FloatField(default=0)),
                ('f2_a50', models.FloatField(default=0)),
                ('f2_a56', models.FloatField(default=0)),
                ('f2_a57', models.FloatField(default=0)),
                ('f2_a58', models.FloatField(default=0)),
                ('f2_a59', models.FloatField(default=0)),
                ('f2_a60', models.FloatField(default=0)),
                ('d3_q', models.CharField(max_length=13)),
                ('d3_k', models.CharField(max_length=30)),
                ('f3_q', models.CharField(max_length=13)),
                ('f3_k_a', models.CharField(max_length=34)),
                ('f3_a79', models.FloatField(default=0)),
                ('f3_a80', models.FloatField(default=0)),
                ('f3_a81', models.FloatField(default=0)),
                ('f3_a82', models.FloatField(default=0)),
                ('f3_a83', models.FloatField(default=0)),
                ('f3_a84', models.FloatField(default=0)),
                ('f3_a85', models.FloatField(default=0)),
                ('cem', models.FloatField()),
            ],
            options={
                'ordering': ['-cem'],
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sınaq başlığı')),
                ('exam_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='İmtahan haqqında')),
                ('exam_fee', models.IntegerField(verbose_name='İmtahan qiyməti')),
                ('exam_date', models.DateField(verbose_name='İmtahan tarixi')),
                ('exam_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sınaq keçiriləcək ünvan')),
                ('exam_img', models.ImageField(blank=True, null=True, upload_to='exam/', verbose_name='Reklam üçün şəkil')),
                ('is_active', models.BooleanField(default=False, verbose_name='Əsas səhifədə görünürlük')),
            ],
            options={
                'ordering': ['-exam_date'],
            },
        ),
        migrations.CreateModel(
            name='ExamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, verbose_name='İmtahan kateqoriyası')),
                ('is_active', models.BooleanField(default=False, verbose_name='Əsas səhifədə görünürlük')),
            ],
        ),
        migrations.CreateModel(
            name='Sinaqlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinaq_nov', models.CharField(choices=[('asagisinif', 'Aşağı siniflər'), ('blok9_10', 'Blok 9 və 10-cu siniflər'), ('blok11', 'Blok 11-ci sinif'), ('buraxilis9', 'Buraxılış 9-cu sinif'), ('buraxilis10', 'Buraxılış 10'), ('buraxilis11', 'Buraxılış 11')], max_length=100)),
                ('sinaq_duzgun_cvb', models.TextField()),
                ('sinaq_sagird_cvb', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
                ('sinaq_tarix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.exam', verbose_name='Sınaq adı')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', ckeditor.fields.RichTextField(verbose_name='Mövzu')),
                ('exam_title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='info.exam', verbose_name='Sınaq seç')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.examcategory', verbose_name='Kateqoriya seç'),
        ),
    ]
