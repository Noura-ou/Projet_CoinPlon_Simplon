# Generated by Django 4.1.2 on 2022-10-10 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('external_page', models.URLField(blank=True)),
                ('button_text', models.CharField(blank=True, max_length=50)),
                ('internal_page', models.ForeignKey(blank=True, help_text='Sélectionner une page interne', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('service_image', models.ForeignKey(help_text='Choisir une image pour ce service', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='ServicesPage',
        ),
    ]
