# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=50)),
                ('category_id', models.IntegerField(default=None)),
                ('sub_category_id', models.IntegerField(default=None)),
                ('price', models.IntegerField(default=0)),
                ('available_quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locality_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
                ('city', models.ForeignKey(to='profile_manager.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider_name', models.CharField(max_length=50)),
                ('provider_description', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField(default=0)),
                ('landmark', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
                ('city_id', models.ForeignKey(to='profile_manager.City')),
                ('country_id', models.ForeignKey(to='profile_manager.Country')),
                ('locality_id', models.ForeignKey(to='profile_manager.Locality')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=b'Created At')),
                ('deleted_at', models.DateTimeField(verbose_name=b'Deleted At')),
                ('modified_at', models.DateTimeField(verbose_name=b'Modified At')),
                ('modified_by', models.IntegerField(default=1)),
                ('country', models.ForeignKey(to='profile_manager.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='provider',
            name='state_id',
            field=models.ForeignKey(to='profile_manager.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='provider',
            field=models.ForeignKey(to='profile_manager.Provider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='profile_manager.State'),
            preserve_default=True,
        ),
    ]
