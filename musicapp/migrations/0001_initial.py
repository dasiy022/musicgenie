# Generated by Django 4.1.1 on 2022-11-12 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('nationality', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(null=True)),
                ('album', models.CharField(max_length=80, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artist')),
            ],
        ),
    ]
