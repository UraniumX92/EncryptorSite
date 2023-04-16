# Generated by Django 4.1.7 on 2023-04-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('operation', models.CharField(max_length=7)),
                ('save_job', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=120)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
