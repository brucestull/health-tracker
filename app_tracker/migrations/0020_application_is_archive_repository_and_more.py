# Generated by Django 4.1.9 on 2023-08-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracker', '0019_application_is_official_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_archive_repository',
            field=models.BooleanField(default=False, help_text='Whether or not the application is a repository for an archived app that is no longer maintained.', verbose_name='Is Archive Repository'),
        ),
        migrations.AlterField(
            model_name='application',
            name='is_official_repository',
            field=models.BooleanField(default=False, help_text='Whether or not the application is a repository for an official app maintained by some other organization.', verbose_name='Is Official Repository'),
        ),
        migrations.AlterField(
            model_name='application',
            name='project',
            field=models.ManyToManyField(blank=True, help_text='The project(s) that the application is associated with.', related_name='applications', to='app_tracker.project', verbose_name='Project'),
        ),
    ]