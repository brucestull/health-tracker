# Generated by Django 4.1.7 on 2023-11-26 10:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cbt", "0005_remove_thought_cognative_distortion_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CognativeDistortion",
            new_name="CognitiveDistortion",
        ),
    ]
