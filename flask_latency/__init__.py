import time
import random

class Latency(object):
    def __init__(self, app):
        self.app = app

        if not self.is_enabled():
            return

        # a tuple range, or int, in seconds
        self.latency_pre = app.config.get('FAKE_LATENCY_BEFORE', None)
        self.latency_post = app.config.get('FAKE_LATENCY_AFTER', None)

        app.before_request(self.before_request)
        app.after_request(self.after_request)

    def is_enabled(self):
        # Only fake latency in debug mode. Adding latency on production is just dumb!
        return self.app.debug

    def is_enabled_request(self):
        # Ability to enable/disable latency based on the request context
        # Override this to selectively enable latency based on request.url
        return True

    def before_request(self):
        if self.latency_pre and self.is_enabled_request():
            self.apply_latency(self.latency_pre)

    def after_request(self, response):
        if self.latency_post and self.is_enabled_request():
            self.apply_latency(self.latency_post)
        return response

    def apply_latency(self, amount):
        if isinstance(amount, tuple):
            amount = random.uniform(amount[0], amount[1])
        time.sleep(amount)
