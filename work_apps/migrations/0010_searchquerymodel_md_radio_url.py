# Generated by Django 2.2.4 on 2020-12-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_apps', '0009_searchquerymodel_md_seller_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_radio_url',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
