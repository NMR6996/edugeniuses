# Generated by Django 4.2.7 on 2023-12-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buraxilis9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinaq_no', models.CharField(max_length=100)),
                ('aad', models.CharField(max_length=12)),
                ('soyad', models.CharField(max_length=12)),
                ('is_no', models.CharField(max_length=6)),
                ('sinif', models.CharField(max_length=2)),
                ('d1_q', models.CharField(max_length=23)),
                ('f1_q', models.CharField(max_length=23)),
                ('f1_a6', models.FloatField(default=0)),
                ('f1_a28', models.FloatField(default=0)),
                ('f1_a29', models.FloatField(default=0)),
                ('f1_a30', models.FloatField(default=0)),
                ('d2_q', models.CharField(max_length=20)),
                ('f2_q', models.CharField(max_length=20)),
                ('f2_a49', models.FloatField(default=0)),
                ('f2_a50', models.FloatField(default=0)),
                ('f2_a59', models.FloatField(default=0)),
                ('f2_a60', models.FloatField(default=0)),
                ('d3_q', models.CharField(max_length=13)),
                ('d3_k', models.CharField(max_length=30)),
                ('f3_q', models.CharField(max_length=13)),
                ('f3_k_a', models.CharField(max_length=34)),
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
    ]
