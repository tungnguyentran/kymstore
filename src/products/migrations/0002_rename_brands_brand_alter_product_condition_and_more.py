# Generated by Django 4.2.7 on 2023-11-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brands',
            new_name='Brand',
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New Tag', 'New Tag'), ('Used', 'Used'), ('Like new', 'Like new'), ('Old', 'Old')], default='New Tag', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Ready for renting'), (1, 'Being rented'), (2, 'Washing')], default=0),
        ),
    ]