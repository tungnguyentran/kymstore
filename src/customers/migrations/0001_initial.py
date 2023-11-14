# Generated by Django 4.2.7 on 2023-11-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]