# Generated by Django 3.0.6 on 2020-05-25 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=128)),
                ('middle_name', models.CharField(default='', max_length=128)),
                ('last_name', models.CharField(default='', max_length=128)),
                ('home_no', models.CharField(max_length=64)),
                ('mobile_no', models.CharField(max_length=64)),
                ('address_line_1', models.CharField(default='', max_length=255)),
                ('address_line_2', models.CharField(default='', max_length=255)),
                ('address_line_3', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=128)),
                ('postcode', models.CharField(default='', max_length=64)),
                ('country', django_countries.fields.CountryField(default=None, max_length=2, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
