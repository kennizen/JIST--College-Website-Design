# Generated by Django 2.2.4 on 2019-09-26 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_stuinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userInfo'),
        ),
    ]
