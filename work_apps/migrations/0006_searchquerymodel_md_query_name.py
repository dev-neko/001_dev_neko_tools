# Generated by Django 2.2.4 on 2020-12-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_apps', '0005_auto_20201209_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_query_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]