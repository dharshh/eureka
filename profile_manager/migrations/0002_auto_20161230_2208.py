# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
                ('published', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategory_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
                ('published', models.BooleanField(default=0)),
                ('category', models.ForeignKey(to='profile_manager.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='sub_category_id',
        ),
        migrations.AddField(
            model_name='city',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='diff_flag',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='subcategory_id',
            field=models.ForeignKey(default=None, to='profile_manager.Subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locality',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='category_id',
            field=models.ForeignKey(default=None, to='profile_manager.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='diff_flag',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='subcategory_id',
            field=models.ForeignKey(default=None, to='profile_manager.Subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='category_id',
            field=models.ForeignKey(to='profile_manager.Category'),
        ),
    ]
