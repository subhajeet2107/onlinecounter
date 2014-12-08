# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(verbose_name=b'IP Address', db_column=b'visitor_ip')),
                ('visited_time', models.TimeField(auto_now_add=True, verbose_name=b'Visited Time', db_column=b'visitor_time')),
            ],
            options={
                'db_table': 'online_counter',
                'verbose_name_plural': 'Online Counter',
            },
            bases=(models.Model,),
        ),
    ]
