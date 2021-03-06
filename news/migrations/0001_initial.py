# Generated by Django 3.0.5 on 2020-04-04 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Категория')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(max_length=5000)),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveIntegerField(default=2019, verbose_name='Дата выхода')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False)),
                ('avtor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='news_avtor', to=settings.AUTH_USER_MODEL, verbose_name='avtor')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Category')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'Newses',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Tag')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Review')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.RatingStar')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='NewsShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news_shots/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
            options={
                'verbose_name': 'Кадр',
                'verbose_name_plural': 'Кадры',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='news.Tag'),
        ),
    ]
