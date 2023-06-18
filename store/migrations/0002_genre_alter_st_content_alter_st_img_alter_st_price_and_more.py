# Generated by Django 4.0.5 on 2022-07-23 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='st',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='st',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='st',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='st',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='st',
            name='title',
            field=models.CharField(help_text='Enter field documentation', max_length=35, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='st',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.genre', verbose_name='Рубрика'),
        ),
    ]
