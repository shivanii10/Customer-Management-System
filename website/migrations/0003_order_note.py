# Generated by Django 3.0.5 on 2020-11-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
