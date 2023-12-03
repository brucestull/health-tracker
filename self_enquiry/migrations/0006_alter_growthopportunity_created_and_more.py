# Generated by Django 4.1.9 on 2023-08-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_enquiry', '0005_alter_growthopportunity_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growthopportunity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time the growth opportunity was created.'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='created',
            field=models.DateTimeField(help_text='The date and time the journal was created.'),
        ),
    ]
