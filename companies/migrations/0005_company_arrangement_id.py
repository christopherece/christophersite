# Generated by Django 4.2.2 on 2024-10-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_title_alter_experience_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='arrangement_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
