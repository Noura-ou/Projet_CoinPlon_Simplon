# Generated by Django 4.1.2 on 2022-10-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='sous titre sous la bannière', max_length=140),
        ),
    ]
