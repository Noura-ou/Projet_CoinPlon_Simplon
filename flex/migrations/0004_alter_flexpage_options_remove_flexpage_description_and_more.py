# Generated by Django 4.1.2 on 2022-10-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_flexpage_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flexpage',
            options={'verbose_name': 'Page divers', 'verbose_name_plural': 'Pages divers'},
        ),
        migrations.RemoveField(
            model_name='flexpage',
            name='description',
        ),
        migrations.AddField(
            model_name='flexpage',
            name='text',
            field=models.TextField(blank=True, default='Etincidunt dolore magnam aliquam etincidunt adipisci dolorem modi. Dolorem amet neque ipsum dolorem. Ipsum sit ipsum dolorem neque eius ut. Neque tempora quiquia ut sed. Velit est porro labore voluptatem neque sit magnam. Aliquam amet etincidunt quisquam sed. Dolor consectetur numquam dolor aliquam amet dolore quaerat. Quiquia aliquam ipsum quiquia dolorem adipisci sed.', max_length=600, null=True),
        ),
    ]
