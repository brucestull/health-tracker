# Generated by Django 4.1.7 on 2023-09-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0004_alter_thought_cognative_distortion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thought',
            name='cognative_distortion',
        ),
        migrations.AddField(
            model_name='thought',
            name='cognative_distortion',
            field=models.ManyToManyField(help_text='The cognative distortion of the thought.', related_name='thoughts', to='cbt.cognativedistortion'),
        ),
    ]