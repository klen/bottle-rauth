import bottle

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


@app.route('/')
def index():
    return '<a href="/github">Login with github</a>'


@app.route('/github', provider='github')
def github(rauth):
    info = rauth.get('user').json()
    info['token'] = rauth.access_token
    return info

if __name__ == '__main__':
    app.run(port=5000)
