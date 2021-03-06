import rauth
from bottle import request, redirect
from copy import copy

__version__ = "0.1.1"
__project__ = "bottle-rauth"
__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "MIT"


class RAuthPlugin(object):

    """ Support RAuth for bottle. """

    name = 'rauth'
    api = 2

    def __init__(self, **options):
        self.options = options

    def setup(self, app):
        app.config.setdefault('RAUTH', self.options)
        self.options = app.config['RAUTH']

    def apply(self, callback, route):
        def wrapper(*args, **kwargs):
            if self.name in route.get_callback_args():
                provider = route.config['provider']
                config = copy(self.options[provider])
                params = config.pop('params', {})
                params['redirect_uri'] = request.url

                service = rauth.OAuth1Service
                if config.pop('type', None) == 'oauth2':
                    service = rauth.OAuth2Service
                service = service(**config)

                if 'code' not in request.params:
                    redirect(service.get_authorize_url(**params))

                kwargs[self.name] = service.get_auth_session(data={
                    'code': request.params.get('code'),
                    'redirect_uri': request.url,
                })

            return callback(*args, **kwargs)
        return wrapper


# pylama:ignore=R0201
