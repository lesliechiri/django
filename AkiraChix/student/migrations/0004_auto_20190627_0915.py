# Generated by Django 2.2.1 on 2019-06-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]