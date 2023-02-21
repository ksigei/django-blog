# Generated by Django 4.1.7 on 2023-02-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('content', models.TextField(default=True)),
                ('image', models.FileField(upload_to='media')),
            ],
        ),
    ]
