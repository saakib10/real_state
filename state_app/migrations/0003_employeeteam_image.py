# Generated by Django 3.1.7 on 2021-10-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state_app', '0002_employeeteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeteam',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]