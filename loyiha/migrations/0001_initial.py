# Generated by Django 3.2.9 on 2021-11-23 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ishchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=400)),
                ('familiyasi', models.CharField(max_length=400)),
                ('qayerda_oqigan', models.CharField(max_length=400)),
                ('qayerda_ishlagan', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Talabalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=100)),
                ('familiyasi', models.CharField(max_length=100)),
                ('otasi_ismi', models.CharField(max_length=100)),
                ('rasmi', models.ImageField(upload_to='')),
                ('qachon_oqigan', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Loyiha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=400)),
                ('sisilka', models.CharField(max_length=400)),
                ('rasmi', models.ImageField(upload_to='')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loyiha.talabalar')),
            ],
        ),
    ]
