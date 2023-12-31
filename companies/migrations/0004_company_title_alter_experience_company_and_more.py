# Generated by Django 4.2.2 on 2023-08-29 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
