# Generated by Django 4.2.2 on 2023-08-18 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_logo_alter_company_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company')),
            ],
        ),
    ]