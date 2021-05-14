# https://spotipy.readthedocs.io/en/2.18.0/

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f4995b37c45547258b6f0b92e411a059",
                                                           client_secret="2029ff44c5f446d194eb6345dcc8f1b7"))

# get the top 20 tracks from Lady Gaga
results = sp.search(q='lady gaga', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx+1, track['name'])

