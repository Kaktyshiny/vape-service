# Generated by Django 2.1.7 on 2019-04-05 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0010_auto_20190405_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='out',
            name='volume',
        ),
        migrations.AlterField(
            model_name='out',
            name='name_ex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad.Liquids', verbose_name='жидкость'),
        ),
    ]
