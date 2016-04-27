from flask import render_template, Flask
from datafoo import spotify

app = Flask(__name__)

@app.route('/')
def homepage():
    html = render_template('homepage.html')
    return html

@app.route('/search/<name>')
def search(name):
    data = spotify.search_by_artist_name(name)
    api_url = data['artists']['href']
    items = data['artists']['items']
    html = render_template('search.html',
                            artist_name=name,
                            results=items,
                            api_url=api_url)
    return html




@app.route('/artist/<id>')
def artist(id):
    artist = spotify.get_artist(id)

    if artist['images']:
        image_url = artist['images'][0]['url']
    else:
        image_url = 'http://placecage.com/600/400'

    tracksdata = spotify.get_artist_top_tracks(id)
    tracks = tracksdata['tracks']

    artistsdata = spotify.get_related_artists(id)
    relartists = artistsdata['artists']
    html = render_template('artist.html',
                            artist=artist,
                            related_artists=relartists,
                            image_url=image_url,
                            tracks=tracks)
    return html



if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)


