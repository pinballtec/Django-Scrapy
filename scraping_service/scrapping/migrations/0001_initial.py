# Generated by Django 3.0.14 on 2023-03-01 19:06

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import scrapping.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='City Name')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'City collection',
            },
        ),
        migrations.CreateModel(
            name='Errors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', jsonfield.fields.JSONField(default=dict)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programming_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Programming Language')),
                ('slug', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Programming language collection',
            },
        ),
        migrations.CreateModel(
            name='Job_Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.URLField(unique=True)),
                ('title', models.CharField(max_length=30, verbose_name='Name of job offer')),
                ('company', models.CharField(max_length=15, verbose_name='Name of the company')),
                ('description', models.TextField(verbose_name='Job description of the vacancy')),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapping.City')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapping.Programming_Language')),
            ],
            options={
                'verbose_name': 'Job offers collection model',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_data', jsonfield.fields.JSONField(default=scrapping.models.default_url)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapping.City', verbose_name='City')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapping.Programming_Language', verbose_name='Programming Language')),
            ],
            options={
                'unique_together': {('city', 'language')},
            },
        ),
    ]
