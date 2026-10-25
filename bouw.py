"""Bouwt playlist.m3u uit bronnen.txt en eigen-zenders.m3u."""
import re
import sys
import urllib.request
from pathlib import Path

MAP = Path(__file__).parent
UITVOER = MAP / "playlist.m3u"


def lees_m3u(tekst):
    """Geeft (extinf-regel, url) paren terug."""
    items, info = [], None
    for regel in tekst.splitlines():
        regel = regel.strip()
        if regel.startswith("#EXTINF"):
            info = regel
        elif regel and not regel.startswith("#") and info:
            items.append((info, regel))
            info = None
    return items


def zet_groep(info, groep):
    info = re.sub(r'\s*group-title="[^"]*"', "", info)
    return info.replace("#EXTINF:-1", f'#EXTINF:-1 group-title="{groep}"', 1)


def haal_op(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def main():
    zenders, gezien = [], set()

    def voeg_toe(items, groep):
        for info, url in items:
            if url not in gezien:
                gezien.add(url)
                zenders.append((zet_groep(info, groep), url))

    eigen = MAP / "eigen-zenders.m3u"
    if eigen.exists():
        voeg_toe(lees_m3u(eigen.read_text(encoding="utf-8")), "Eigen zenders")

    for regel in (MAP / "bronnen.txt").read_text(encoding="utf-8").splitlines():
        regel = regel.strip()
        if not regel or regel.startswith("#") or "|" not in regel:
            continue
        groep, url = (d.strip() for d in regel.split("|", 1))
        try:
            items = lees_m3u(haal_op(url))
        except Exception as fout:
            print(f"Overgeslagen: {groep} ({fout})", file=sys.stderr)
            continue
        voeg_toe(items, groep)
        print(f"{groep}: {len(items)} zenders")

    regels = ["#EXTM3U"]
    for info, url in zenders:
        regels += [info, url]
    UITVOER.write_text("\n".join(regels) + "\n", encoding="utf-8")
    print(f"Klaar: {len(zenders)} zenders in {UITVOER.name}")


if __name__ == "__main__":
    main()
