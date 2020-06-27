# Generated by Django 3.0.7 on 2020-06-26 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20200626_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinasInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID da Disciplina', primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Disciplinas')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
