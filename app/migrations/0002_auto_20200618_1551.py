# Generated by Django 3.0.7 on 2020-06-18 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinas',
            name='requisitos',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='app.Disciplinas'),
        ),
    ]
