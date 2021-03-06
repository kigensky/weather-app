# Generated by Django 3.2.8 on 2021-10-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days_of_the_week', models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Teusday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=0)),
                ('Rainfall', models.FloatField()),
                ('Day_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-Day_created'],
            },
        ),
    ]
