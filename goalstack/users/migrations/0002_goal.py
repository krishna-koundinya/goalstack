# Generated by Django 3.1.1 on 2021-01-30 18:20

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('goal', models.CharField(max_length=255, verbose_name='Goal Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Goal Address')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('goal_type', models.CharField(choices=[('unspecified', 'Unspecified'), ('time-based', 'Time-Based'), ('count-based', 'Count-Based'), ('abstain', 'abstain')], default='unspecified', max_length=20, verbose_name='Goal Type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]