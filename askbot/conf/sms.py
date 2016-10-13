"""
External service key settings
"""
from askbot.conf.settings_wrapper import settings
from askbot.conf.super_groups import LOGIN_USERS_COMMUNICATION
from askbot.deps import livesettings
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
from askbot.skins import utils as skin_utils
from askbot.utils.loading import module_exists

SMS_SETTINGS = livesettings.ConfigurationGroup(
                    'SMS_SETTINGS',
                    _('SMS settings'),
                    super_group = LOGIN_USERS_COMMUNICATION
                )

settings.register(
    livesettings.BooleanValue(
        SMS_SETTINGS,
        'ENABLE_SMS_REGISTRATION',
        default=False,
        description=_('Enable registration with mobile phone and sms'),
        help_text=_("Extra setup is required in the external keys section")
    )
)

SMS_BACKEND_HOICES = (
    ('twilio', 'Twilio sms backend'),
)

settings.register(
    livesettings.StringValue(
        SMS_SETTINGS,
        'SMS_BACKEND',
        default='',
        description=_('SMS gateway provider'),
        choices=SMS_BACKEND_HOICES,
        help_text=_("Extra setup is required in the external keys section")
    )
)

settings.register(
    livesettings.StringValue(
        SMS_SETTINGS,
        'SMS_DEFAULT_FROM_NUMBER',
        default='',
        description=_('SMS default from number'),
    )
)
