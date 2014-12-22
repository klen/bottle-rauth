""" Tests for `bottle-oauth` module. """


def test_bottle_rauth():
    import bottle
    import webtest
    from bottle_rauth import RAuthPlugin

    app = bottle.Bottle()
    app.install(RAuthPlugin(github={
        'type': 'oauth2',
        'client_id': 'e8f9ebe239374201c0fc',
        'client_secret': 'b541a98555a0e01a85baef38dd2859d7335eba68',
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
