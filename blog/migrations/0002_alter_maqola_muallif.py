# Generated by Django 4.1.1 on 2022-11-04 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqola',
            name='muallif',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.muallif'),
        ),
    ]
