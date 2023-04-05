# Generated by Django 4.2 on 2023-04-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('score', models.IntegerField(blank=True, default=75, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_key_skill', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
