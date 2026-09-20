#!/usr/bin/env python3
"""genera-wordmark.py — il marchio «Cyber Boomer» disegnato, non scaricato.

    python3 scripts/genera-wordmark.py            # scrive wordmark.svg e favicon.svg
    python3 scripts/genera-wordmark.py --inline   # stampa l'SVG da incollare in una pagina

L'ARCHITETTURA DEL MARCHIO, approvata a voce dal Direttore l'08/08 e mai scritta
fino al 20/09: «Cyber» elegante · «Boomer» 8-bit · lo spirito in mezzo. Boomer è il
nome, Cyber il cognome (decisione del 26/07): il nome è quello che la gente pronuncia,
e qui è fatto di blocchi, come le prime lettere che uno schermo abbia mai mostrato.
Il cognome sta sopra, in corsivo leggero, come una firma su una fotografia.

PERCHÉ UN GENERATORE E NON UN FILE DISEGNATO A MANO: la casa non scarica caratteri da
fuori (il guardiano lo misura), quindi «Boomer» in 8-bit non può venire da un font. Viene
da una mappa di bit scritta qui sotto, 5 colonne × 7 righe per lettera, disegnata da JUDY:
non è la copia di nessun carattere esistente. Cambiare una lettera è cambiare una riga
di asterischi. Il corsivo di «Cyber» usa i caratteri che il lettore ha già in casa.

I colori sono SOLO i token di stile.css: carta per le lettere, blu link per il punto
che lampeggia. Nessun colore di altre case.

— creato da JUDY, 2026-09-20
"""
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent

# ── la mappa di bit: 5×7, «*» pieno, «.» vuoto — disegnata qui, non copiata ──
BIT = {
    'B': ["****.", "*...*", "*...*", "****.", "*...*", "*...*", "****."],
    'O': [".***.", "*...*", "*...*", "*...*", "*...*", "*...*", ".***."],
    'M': ["*...*", "**.**", "*.*.*", "*.*.*", "*...*", "*...*", "*...*"],
    'E': ["*****", "*....", "*....", "****.", "*....", "*....", "*****"],
    'R': ["****.", "*...*", "*...*", "****.", "*.*..", "*..*.", "*...*"],
}

CARTA = "#EFE6EB"   # --text-hi
BLU   = "#5C7CFF"   # --voice
NERO  = "#0C0A0C"   # --bg-deep

def blocchi(parola, x0, y0, u, colore, gap=1):
    """Rettangoli SVG per una parola in 8-bit. u = lato del blocco, gap = colonne vuote fra lettere."""
    out = []
    x = x0
    for ch in parola:
        m = BIT[ch]
        for r, riga in enumerate(m):
            for c, bit in enumerate(riga):
                if bit == '*':
                    out.append(f'<rect x="{x + c*u}" y="{y0 + r*u}" width="{u}" height="{u}" fill="{colore}"/>')
        x += (5 + gap) * u
    return out, x - gap*u  # larghezza consumata

def wordmark_svg(inline=False):
    """Il marchio intero: «Cyber» in corsivo di sistema sopra, «Boomer» in blocchi sotto,
    e il punto blu che lampeggia (via CSS: .wm-punto). Misure in unità di blocco."""
    u = 8                       # lato del blocco
    lettere, larg = blocchi("BOOMER", 0, 0, u, CARTA)
    alt_boomer = 7 * u          # 56
    alt_cyber = 4 * u           # spazio per il corsivo sopra
    W = larg + 2*u + u          # spazio per il punto a destra
    H = alt_cyber + alt_boomer
    # «Cyber»: testo in corsivo con i caratteri di casa; misura e stile li dà il CSS della pagina
    cyber = (f'<text class="wm-cyber" x="0" y="{alt_cyber - u//2}" font-size="{int(2.6*u)}" '
             f'fill="{CARTA}" font-style="italic" font-weight="300" '
             f'font-family="\'Iowan Old Style\',\'Palatino Linotype\',Palatino,Georgia,serif">Cyber</text>')
    boomer = f'<g transform="translate(0,{alt_cyber})">' + ''.join(lettere) + '</g>'
    punto = (f'<rect class="wm-punto" x="{larg + u}" y="{alt_cyber + 5*u}" width="{u}" height="{2*u}" '
             f'fill="{BLU}"/>')
    attrs = 'role="img" aria-label="Cyber Boomer"'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
           f'{attrs} shape-rendering="crispEdges">{cyber}{boomer}{punto}</svg>')
    if inline:
        svg = svg.replace(' xmlns="http://www.w3.org/2000/svg"', '', 1)
    return svg

def favicon_svg():
    """La B del nome, in blocchi, col punto blu: la stessa mappa, 64×64."""
    u = 7
    lettere, larg = blocchi("B", 12, 8, u, CARTA)
    punto = f'<rect x="{12 + 5*u + 4}" y="{8 + 5*u}" width="{u}" height="{2*u}" fill="{BLU}"/>'
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Cyber Boomer" '
            'shape-rendering="crispEdges">\n'
            '  <!-- La B di Boomer in blocchi, dalla stessa mappa di bit del marchio (scripts/genera-wordmark.py),\n'
            '       e il punto blu che sul sito lampeggia. Chi ci trova un ninja, ci trova un ninja. -->\n'
            f'  <rect width="64" height="64" rx="12" fill="{NERO}"/>\n'
            '  ' + ''.join(lettere) + punto + '\n</svg>\n')

if __name__ == '__main__':
    if '--inline' in sys.argv:
        print(wordmark_svg(inline=True)); sys.exit(0)
    (RADICE / 'wordmark.svg').write_text(wordmark_svg() + '\n', encoding='utf-8')
    (RADICE / 'favicon.svg').write_text(favicon_svg(), encoding='utf-8')
    print("wordmark.svg e favicon.svg scritti")
