# Generated by Django 4.1.7 on 2023-03-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=332, verbose_name='shop name :')),
                ('title', models.CharField(max_length=444, verbose_name='product title')),
                ('txt', models.TextField(verbose_name='product info ')),
                ('img', models.ImageField(upload_to='media', verbose_name='product image:')),
                ('sale', models.ImageField(null=True, upload_to='media', verbose_name='product sale:')),
            ],
            options={
                'verbose_name': 'generalslider',
                'verbose_name_plural': 'generalslider',
            },
        ),
        migrations.CreateModel(
            name='GeneralSliderActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=332, verbose_name='shop name :')),
                ('title', models.CharField(max_length=444, verbose_name='product title')),
                ('txt', models.TextField(verbose_name='product info ')),
                ('img', models.ImageField(upload_to='media', verbose_name='product image:')),
                ('sale', models.ImageField(null=True, upload_to='media', verbose_name='product sale:')),
            ],
            options={
                'verbose_name': 'generalslideractive',
                'verbose_name_plural': 'generalslideractive',
            },
        ),
    ]
