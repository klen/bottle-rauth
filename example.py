import bottle

from bottle_rauth import RAuthPlugin


app = bottle.Bottle()
app.config['RAUTH'] = {
    'github': {
        'type': 'oauth2',
        'client_id': 'e8f9ebe239374201c0fc',
        'client_secret': 'b541a98555a0e01a85baef38dd2859d7335eba68',
        'authorize_url': 'https://github.com/login/oauth/authorize',
        'access_token_url': 'https://github.com/login/oauth/access_token',
        'base_url': 'https://api.github.com/',
        'params': {
            'scope': 'user:email',
        }
    }
}
app.install(RAuthPlugin())


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
