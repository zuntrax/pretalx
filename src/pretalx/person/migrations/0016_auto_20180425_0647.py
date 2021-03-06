# Generated by Django 2.0.3 on 2018-04-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0015_speakerinformation_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', help_text='Please enter the name you wish to be displayed publically.', max_length=120, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
