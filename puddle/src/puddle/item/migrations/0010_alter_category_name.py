# Generated by Django 4.2.7 on 2023-12-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]