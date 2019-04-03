# Generated by Django 2.1.1 on 2019-02-18 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190202_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-release_date']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ['-release_Date']},
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='First_Name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Record_Label',
            new_name='record_Label',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='No_of_Album',
            new_name='so_of_album',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Stage_Name',
            new_name='stage_name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Surname',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Artist_Name',
            new_name='artist_name',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Music',
            new_name='music',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Music_Name',
            new_name='music_name',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Release_Date',
            new_name='release_date',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='Artist',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='Release_Date',
            new_name='release_Date',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='Video',
            new_name='video',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='First_Name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='Surname',
            new_name='surname',
        ),
    ]
