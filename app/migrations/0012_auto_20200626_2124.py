# Generated by Django 3.0.7 on 2020-06-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200626_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinas',
            name='requisitos',
            field=models.ManyToManyField(blank=True, null=True, to='app.Disciplinas'),
        ),
    ]
