# Generated by Django 2.1 on 2018-08-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_common', '0005_auto_20180725_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcolumnmap',
            name='provider_type',
            field=models.CharField(choices=[('AWS', 'AWS'), ('Local', 'Local')], default='AWS', max_length=50),
        ),
    ]
