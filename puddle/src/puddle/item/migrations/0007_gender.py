# Generated by Django 4.2.7 on 2023-12-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_rename_category_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
