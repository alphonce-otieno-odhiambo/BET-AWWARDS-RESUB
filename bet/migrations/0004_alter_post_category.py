# Generated by Django 3.2.9 on 2022-01-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_auto_20220113_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Designe', 'Designe'), ('Informative', 'Informative'), ('Functionality', 'Functionality')], default='Designe', max_length=60, null=True),
        ),
    ]