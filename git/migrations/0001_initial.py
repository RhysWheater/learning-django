# Generated by Django 4.2.2 on 2023-06-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo', models.CharField(max_length=200)),
                ('commit_id', models.CharField(max_length=200)),
            ],
        ),
    ]
