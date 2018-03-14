# Generated by Django 2.0.1 on 2018-03-07 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
                ('author_date', models.DateTimeField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_body', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='blogbook',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myBlog.Category'),
        ),
        migrations.AddField(
            model_name='blogbook',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myBlog.Tag'),
        ),
    ]