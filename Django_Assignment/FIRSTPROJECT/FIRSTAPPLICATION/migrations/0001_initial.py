# Generated by Django 3.2.5 on 2021-07-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Contact', models.CharField(max_length=12)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
