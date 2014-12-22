""" Tests for `bottle-oauth` module. """


def test_bottle_rauth():
    import bottle
    import webtest
    from bottle_rauth import RAuthPlugin

    app = bottle.Bottle()
    app.install(RAuthPlugin(github={
        'type': 'oauth2',
        'client_id': 'e3e297bb9f506cbea557',
        'client_secret': 'd113380beb8f1ed8a77b688e2b81b76c9be00d09',
        'authorize_url': 'https://github.com/login/oauth/authorize',
        'access_token_url': 'https://github.com/login/oauth/access_token',
        'base_url': 'https://api.github.com/',
    }))

    @app.route('/github', provider='github')
    def github(rauth):
        return "OK"

    client = webtest.TestApp(app)
    response = client.get('/github')
    assert response.status_code == 302
