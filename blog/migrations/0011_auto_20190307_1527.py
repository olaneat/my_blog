# Generated by Django 2.1.1 on 2019-03-07 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_news_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('published', 'published'), ('Draft', 'Draft')], max_length=17),
        ),
    ]
