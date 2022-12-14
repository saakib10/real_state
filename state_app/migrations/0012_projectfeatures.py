# Generated by Django 3.1.7 on 2021-11-02 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('state_app', '0011_projects_completed_per'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(blank=True, max_length=100, null=True)),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='state_app.projects')),
            ],
        ),
    ]
