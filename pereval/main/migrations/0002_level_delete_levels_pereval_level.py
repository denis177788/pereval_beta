# Generated by Django 4.2.4 on 2023-11-17 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, max_length=64, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, max_length=64, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, max_length=64, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, max_length=64, null=True, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
            },
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
        migrations.AddField(
            model_name='pereval',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.level'),
            preserve_default=False,
        ),
    ]
