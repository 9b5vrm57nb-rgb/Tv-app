# Mijn IPTV-lijst

Je eigen M3U-lijst. Plak deze link in je IPTV-app (3MU, IPTV Smarters, VLC, ...):

```
https://raw.githubusercontent.com/9b5vrm57nb-rgb/Tv-app/master/playlist.m3u
```

De repository moet daarvoor **openbaar** zijn. Bij een privé-repository werkt de link niet in een app.

## Zo pas je hem aan

- **Lijst van iemand anders toevoegen:** zet een regel in `bronnen.txt`, bijvoorbeeld
  `Kids | https://iptv-org.github.io/iptv/categories/kids.m3u`
- **Losse zender toevoegen:** zet hem in `eigen-zenders.m3u`.
  Ook je eigen betaalde abonnement hoort hier, als je aanbieder je een M3U-adres geeft.

GitHub bouwt `playlist.m3u` automatisch opnieuw na elke wijziging en elke nacht.
Lokaal kan het ook met `python bouw.py`.

Meer gratis lijsten: https://github.com/iptv-org/iptv/blob/master/PLAYLISTS.md

Zet hier alleen streams in die je legaal mag kijken.
