# Generated by Django 4.0.4 on 2022-05-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_block_options_rename_floor_id_room_floor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='room_id',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=True, max_length=50, verbose_name='Course year'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('Faculty of Law and Social Sciences', 'Faculty of Law and Social Sciences'), ('Faculty of Education and Humanities Sciences', 'Faculty of Education and Humanities Sciences'), ('Faculty of Engineering and Natural Sciences', 'Faculty of Engineering and Natural Sciences'), ('Business school', 'Business school')], default='default title', max_length=50, verbose_name='Faculty name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=50, verbose_name='Gender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, verbose_name='Gender'),
        ),
    ]