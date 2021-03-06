# Generated by Django 2.0.4 on 2018-04-21 17:52

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('music', '0003_auto_20180420_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Title')),
                ('comments', models.TextField(blank=True, max_length=500, null=True, verbose_name='Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='GenreThru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music_genrethru_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music_genrethru_items', to='music.Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='album',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='song',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genres',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='music.GenreThru', to='music.Genre', verbose_name='Genres'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genres',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='music.GenreThru', to='music.Genre', verbose_name='Genres'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genres',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='music.GenreThru', to='music.Genre', verbose_name='Genres'),
        ),
    ]
