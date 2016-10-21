# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askbot', '0013_auto_20161008_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSFeedSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feed_type', models.CharField(max_length=16, choices=[(b'q_all', 'Entire forum'), (b'q_ask', 'Questions that I asked'), (b'q_ans', 'Questions that I answered'), (b'q_sel', 'Individually selected questions'), (b'm_and_c', 'Mentions and comment responses')])),
                ('frequency', models.CharField(default=b'n', max_length=8, choices=[(b'i', 'instantly'), (b'd', 'daily'), (b'w', 'weekly'), (b'n', 'never')])),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('reported_at', models.DateTimeField(null=True)),
                ('subscriber', models.ForeignKey(related_name='sms_notification_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='smsfeedsetting',
            unique_together=set([('subscriber', 'feed_type')]),
        ),
    ]
