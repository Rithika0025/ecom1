# Generated by Django 4.1.4 on 2023-01-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_password', models.CharField(max_length=30)),
                ('customer_address', models.CharField(max_length=300)),
                ('customer_phoneno', models.CharField(max_length=20)),
            ],
        ),
    ]
