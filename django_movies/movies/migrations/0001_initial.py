# Generated by Django 3.0.7 on 2020-06-18 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_en', models.CharField(max_length=150)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateField()),
                ('genre', models.CharField(max_length=150)),
                ('watch_grade', models.CharField(max_length=150)),
                ('score', models.FloatField()),
                ('poster_url', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
    ]