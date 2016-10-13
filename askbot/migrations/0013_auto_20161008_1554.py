# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0012_rename_related_name_to_auth_user_from_Vote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'actividad', 'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='award',
            options={'verbose_name': 'award', 'verbose_name_plural': 'awards'},
        ),
        migrations.AlterModelOptions(
            name='badgedata',
            options={'ordering': ('display_order', 'slug'), 'verbose_name': 'badge data', 'verbose_name_plural': 'badge data'},
        ),
        migrations.AlterModelOptions(
            name='favoritequestion',
            options={'verbose_name': 'favorite question', 'verbose_name_plural': 'favorite questions'},
        ),
        migrations.AlterModelOptions(
            name='postflagreason',
            options={'verbose_name': 'post flag reason', 'verbose_name_plural': 'post flag reasons'},
        ),
        migrations.AlterModelOptions(
            name='postrevision',
            options={'ordering': ('-revision',), 'verbose_name': 'post revision', 'verbose_name_plural': 'post revisions'},
        ),
        migrations.AlterModelOptions(
            name='replyaddress',
            options={'verbose_name': 'reply address', 'verbose_name_plural': 'reply addresses'},
        ),
        migrations.AlterModelOptions(
            name='repute',
            options={'verbose_name': 'repute', 'verbose_name_plural': 'repute'},
        ),
        migrations.AlterModelOptions(
            name='threadtogroup',
            options={'verbose_name': 'thread to group', 'verbose_name_plural': 'threads to groups'},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'vote', 'verbose_name_plural': 'votos'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='emailfeedsetting',
            name='frequency',
            field=models.CharField(default=b'n', max_length=8, choices=[(b'i', 'instantly'), (b'd', 'daily'), (b'w', 'weekly'), (b'n', 'never')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='languages',
            field=models.CharField(default=b'es', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='primary_language',
            field=models.CharField(default=b'es', max_length=16, choices=[(b'es', b'Espanol')]),
        ),
    ]
