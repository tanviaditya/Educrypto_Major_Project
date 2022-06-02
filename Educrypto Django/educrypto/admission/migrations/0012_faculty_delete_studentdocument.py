# Generated by Django 4.0.2 on 2022-03-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0011_alter_sharekey_student_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100)),
                ('faculty_fid', models.CharField(blank=True, max_length=200)),
                ('branch', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(default='123456', max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentDocument',
        ),
    ]