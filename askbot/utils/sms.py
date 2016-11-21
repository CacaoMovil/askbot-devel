from askbot.conf import settings as askbot_settings

class InvalidSMSBackend(Exception):
    pass

class BaseSMSBackend(object):

    def send_sms(self):
        raise NotImplementedError()

class TwilioSMSBackend(object):

    def __init__(self, account, token):
        from twilio.rest import TwilioRestClient
        self.account = account
        self.token = token
        self.client = TwilioRestClient(self.account, self.token)

    def send_sms(self, from_, to, body):
        if type(body) != str:
            body = str(body)
        message = self.client.messages.create(body=body, from_=from_, to=to)
        return message


def get_sms_backend_client():
    if askbot_settings.SMS_BACKEND == 'twilio':
        return TwilioSMSBackend(account=askbot_settings.TWILIO_ACCOUNT_SID,
                                token=askbot_settings.TWILIO_AUTH_TOKEN)
    else:
        raise InvalidSMSBackend

def send_sms(to, message):
    backend = get_sms_backend_client()
    return backend.send_sms(askbot_settings.SMS_DEFAULT_FROM_NUMBER,
                            to, message)

def send_sms_notification(to_user, post, update_activity):
    message = post.as_tweet()
    send_sms(str(to_user.askbot_profile.phone_number), message)
