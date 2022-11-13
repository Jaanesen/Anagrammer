from encodings import utf_8
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="",
                                                           client_secret=""))

pl_id = ['spotify:playlist:3l9fQazoTk9ndX5tYtx8WH',
         'spotify:playlist:3Wu2tmhi3p4rwsC7XEOfXI',
         'spotify:playlist:37i9dQZEVXbMDoHDwVN2tF',
         'spotify:playlist:37i9dQZEVXbJvfa0Yxg7E7',
         'spotify:playlist:37i9dQZF1DX55yuR78Invt',
         'spotify:playlist:0D2IW3x8wd3K1Gfr4dfynn',
         'spotify:playlist:1sSUrWAiO1SpqFnuc88Bci',
         'spotify:playlist:3t95sjyyIvqmjDGaKjfikC',
         'spotify:playlist:2auIIn64ryNJIFNrMwIsWh',
         'spotify:playlist:2PIWm6aMk3atuCaJWO1GeR',
         'spotify:playlist:2YaYELkgMaAiDeolHa4sfC',
         'spotify:playlist:0Ncor000gD8vERjgIcjQ10',
         'spotify:playlist:63LneC0SKU7W3XnSawgzkm',
         'spotify:playlist:6L88HPOCIW0hlWfqtxYx9e',
         'spotify:playlist:5hcdG7sQmlBrmbnFK0qctn',
         'spotify:playlist:4fB98okTna3WiZwb6ZcGDC',
         'spotify:playlist:3LRQ0TLsugRGb9t61BkQC6',
         'spotify:playlist:37i9dQZF1DWXRqgorJj26U',
         'spotify:playlist:1yTR9milriO27ECUCbQ9PT',
         'spotify:playlist:4gVyke7MM0zcFCIoO7yX9H',
         'spotify:playlist:0uwA66YOEJ0HKAbRr7AABO',
         'spotify:playlist:35GTaNVgN3V2ioccgUTQvS']


for playlist in pl_id:

    offset = 0

    f = open("resultater/spotify-uttrekk.txt", "a", encoding="utf_8")

    while True:
        response = sp.playlist_items(playlist,
                                     offset=offset,
                                     fields='items.track.name,total',
                                     additional_types=['track'])

        if len(response['items']) == 0:
            break

        try:
            for n in response["items"]:
                f.write(n["track"]["name"] + "\n")
        except:
            print("An exception occurred")

        # print(response['items'])
        offset = offset + len(response['items'])
        print(offset, "/", response['total'])
    f.close()
