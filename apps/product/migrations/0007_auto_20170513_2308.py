# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-13 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20170513_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetailImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='image/default.png', upload_to='produceImage/Detail')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='\u6240\u5c5e\u5546\u54c1')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u8be6\u60c5\u56fe\u7247',
                'verbose_name_plural': '\u4ea7\u54c1\u8be6\u60c5\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='ProductSingleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='image/default.png', upload_to='produceImage/Single')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='\u6240\u5c5e\u5546\u54c1')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u6807\u9898\u56fe\u7247',
                'verbose_name_plural': '\u4ea7\u54c1\u6807\u9898\u56fe\u7247',
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
