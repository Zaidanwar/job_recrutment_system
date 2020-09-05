# Generated by Django 2.2.6 on 2020-08-20 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_company_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applied_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField()),
                ('applied_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Company_Jobs')),
                ('applied_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
