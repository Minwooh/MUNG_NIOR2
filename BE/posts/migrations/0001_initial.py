# Generated by Django 4.2.4 on 2023-08-11 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='작성일')),
                ('writer', models.ForeignKey(limit_choices_to={'user_type': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='작성일')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('answer_id', models.PositiveIntegerField(default=0, editable=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.question')),
                ('writer', models.ForeignKey(limit_choices_to={'user_type': 'teacher'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
