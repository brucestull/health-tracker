# Generated by Django 4.1.7 on 2023-05-14 08:27

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
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Optional - 100 characters or fewer', max_length=100, null=True, verbose_name='Journal Title')),
                ('content', models.TextField(help_text='Required', verbose_name='Journal Content')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]