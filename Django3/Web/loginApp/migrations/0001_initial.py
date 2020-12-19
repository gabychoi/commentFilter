# Generated by Django 3.1.4 on 2020-12-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_posting',
            fields=[
                ('comment_pk_num', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('post', models.IntegerField()),
                ('comment_id', models.CharField(max_length=50)),
                ('comment_id_image', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=400)),
                ('created', models.CharField(max_length=50)),
                ('bad_comment_bool', models.IntegerField()),
                ('bad_comment_prob', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'comment_db',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Comment_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=400)),
                ('comment_pk_num', models.IntegerField()),
                ('customer_check_point', models.IntegerField()),
                ('customer_opinion', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'report_db',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_pk_num', models.IntegerField()),
                ('user_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'like_db',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('pk_num', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('post_user_image', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=50)),
                ('like', models.IntegerField()),
            ],
            options={
                'db_table': 'photo_db',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('user_email', models.CharField(max_length=50, unique=True)),
                ('user_pwd', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user_image', models.ImageField(upload_to='user_image/')),
                ('penalty_count', models.IntegerField()),
                ('comment_count', models.IntegerField()),
                ('bad_comment_ratio', models.FloatField()),
                ('about', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'user_db',
            },
        ),
    ]
