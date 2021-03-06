# Generated by Django 2.0.5 on 2018-05-23 15:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180523_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpreference',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='userpreference',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='name',
            field=models.CharField(default=uuid.uuid4, max_length=255),
        ),
    ]
