# Generated by Django 3.2.6 on 2021-08-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_review_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id']},
        ),
    ]