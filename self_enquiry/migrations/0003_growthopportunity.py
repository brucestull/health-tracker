# Generated by Django 4.1.7 on 2023-06-30 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('self_enquiry', '0002_journal_updated_alter_journal_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowthOpportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Required', verbose_name='Question')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time the learning opportunity was created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time the learning opportunity was last updated.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_opportunities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Learning Opportunity',
                'verbose_name_plural': 'Learning Opportunities',
            },
        ),
    ]