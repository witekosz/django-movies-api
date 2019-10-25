# Generated by Django 2.2.6 on 2019-10-25 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('released', models.DateField()),
                ('runtime', models.PositiveSmallIntegerField()),
                ('genre', models.TextField()),
                ('director', models.CharField(max_length=200)),
                ('writer', models.TextField()),
                ('actors', models.TextField()),
                ('plot', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('awards', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_api.Movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
