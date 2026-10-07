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

# «Cyber» in Newsreader Italic, peso 300 (Light), corpo ottico 20: OFL 1.1 (Production Type,
# github.com/google/fonts/tree/main/ofl/newsreader). Convertito in tracciati una volta sola con
# fontTools, a corpo 20 sulla linea di base y=28, x=0: il font non entra in casa, la forma sì.
# Per rifarlo: instanziare wght=300 opsz=20, disegnare «Cyber» con SVGPathPen, scala 20/upm, y capovolta.
CYBER_PATH = "M10.47 26.91 9.81 27.43 11.88 24.78H12.2L11.04 27.54Q10.2 27.84 9.13 28.02Q8.06 28.2 7.15 28.2Q5.42 28.2 4.17 27.59Q2.93 26.97 2.27 25.81Q1.6 24.64 1.6 22.98Q1.6 21.49 2.03 20.18Q2.46 18.87 3.26 17.8Q4.06 16.74 5.15 15.97Q6.24 15.2 7.57 14.78Q8.9 14.37 10.4 14.37Q10.97 14.37 11.47 14.42Q11.97 14.47 12.45 14.59Q12.94 14.7 13.45 14.9L12.85 14.86L13.89 14.06H14L13.46 18.49H13.16L12.63 15.36L13.22 16Q12.5 15.42 11.73 15.19Q10.96 14.96 10.02 14.96Q8.7 14.96 7.57 15.35Q6.45 15.75 5.55 16.47Q4.66 17.19 4.03 18.17Q3.4 19.15 3.06 20.33Q2.73 21.5 2.73 22.81Q2.73 24.42 3.28 25.49Q3.83 26.57 4.82 27.11Q5.81 27.65 7.13 27.65Q7.96 27.65 8.82 27.49Q9.69 27.33 10.47 26.91ZM13.98 22.69H13.65Q13.86 21.7 14.13 21.03Q14.4 20.36 14.71 19.96Q15.03 19.56 15.39 19.39Q15.75 19.22 16.14 19.22Q16.35 19.22 16.5 19.31Q16.65 19.41 16.79 19.73Q16.92 20.05 17.06 20.69Q17.21 21.34 17.36 22.46Q17.51 23.58 17.67 25.15Q17.82 26.73 17.97 28.75L17.11 29.7Q16.99 28.17 16.88 26.91Q16.77 25.65 16.66 24.66Q16.56 23.66 16.46 22.91Q16.36 22.15 16.26 21.64Q16.14 20.95 16.06 20.64Q15.98 20.33 15.9 20.25Q15.83 20.16 15.72 20.16Q15.43 20.16 15.14 20.39Q14.85 20.61 14.56 21.16Q14.27 21.71 13.98 22.69ZM17.35 28.97 17.65 28.57Q18.42 27.4 18.97 26.26Q19.53 25.11 19.88 23.98Q20.24 22.84 20.4 21.7Q20.57 20.57 20.54 19.41Q20.74 19.35 20.91 19.33Q21.09 19.3 21.24 19.3Q21.44 19.3 21.53 19.38Q21.61 19.46 21.61 19.68Q21.61 20.23 21.48 20.96Q21.34 21.68 21.07 22.53Q20.8 23.38 20.4 24.33Q20 25.27 19.48 26.28Q18.96 27.3 18.32 28.35Q17.25 30.09 16.27 31.18Q15.29 32.27 14.39 32.77Q13.49 33.28 12.66 33.28Q12.05 33.28 11.75 33.02Q11.46 32.76 11.46 32.37Q11.46 32.03 11.64 31.83Q11.81 31.64 12.05 31.64Q12.13 31.64 12.24 31.72Q12.35 31.81 12.54 32Q12.73 32.19 12.95 32.31Q13.17 32.42 13.42 32.42Q13.89 32.42 14.53 32.03Q15.17 31.64 15.9 30.88Q16.62 30.11 17.35 28.97ZM23.66 25.13Q23.57 25.47 23.52 25.77Q23.47 26.08 23.47 26.34Q23.47 27.01 23.78 27.38Q24.09 27.75 24.71 27.75Q25.31 27.75 25.93 27.4Q26.55 27.04 27.13 26.43Q27.7 25.82 28.15 25.05Q28.6 24.27 28.87 23.42Q29.13 22.58 29.13 21.76Q29.13 20.95 28.83 20.53Q28.53 20.11 27.91 20.11Q27.47 20.11 26.99 20.35Q26.51 20.6 26.04 21.02Q25.57 21.44 25.16 21.96Q24.74 22.49 24.42 23.06Q24.11 23.64 23.94 24.2ZM25.82 14.92Q25.63 14.82 25.41 14.74Q25.19 14.65 24.94 14.57Q24.68 14.48 24.39 14.4L24.44 14.23L26.85 13.79H27.04L24.28 23.04L24.16 22.91Q24.92 21.63 25.64 20.82Q26.36 20 27.05 19.61Q27.73 19.22 28.36 19.22Q29.31 19.22 29.76 19.82Q30.21 20.42 30.21 21.39Q30.21 22.43 29.89 23.43Q29.56 24.43 28.99 25.29Q28.43 26.15 27.71 26.81Q27 27.46 26.23 27.83Q25.46 28.2 24.72 28.2Q23.69 28.2 23.15 27.62Q22.62 27.03 22.62 26.1Q22.62 25.83 22.67 25.55Q22.71 25.27 22.79 24.98ZM35.72 19.72Q35.17 19.72 34.65 20.03Q34.12 20.34 33.67 20.88Q33.21 21.43 32.87 22.14Q32.52 22.86 32.32 23.68Q32.13 24.5 32.13 25.35Q32.13 26.5 32.55 26.94Q32.97 27.37 33.63 27.37Q34.05 27.37 34.49 27.2Q34.93 27.03 35.39 26.55Q35.85 26.08 36.35 25.19L36.74 25.19Q36.16 26.4 35.62 27.05Q35.07 27.7 34.51 27.95Q33.95 28.2 33.3 28.2Q32.68 28.2 32.19 27.94Q31.7 27.69 31.41 27.14Q31.13 26.6 31.13 25.74Q31.13 24.63 31.41 23.63Q31.69 22.64 32.18 21.83Q32.67 21.03 33.3 20.44Q33.93 19.85 34.63 19.53Q35.32 19.22 36.01 19.22Q36.61 19.22 36.98 19.43Q37.36 19.64 37.53 19.98Q37.71 20.32 37.71 20.73Q37.71 21.14 37.57 21.53Q37.42 21.92 37.15 22.22Q36.62 22.45 36.03 22.68Q35.43 22.92 34.79 23.15Q34.14 23.38 33.46 23.61Q32.78 23.84 32.08 24.06L32.11 23.61Q33.36 23.22 34.19 22.9Q35.03 22.57 35.54 22.3Q36.05 22.03 36.32 21.78Q36.58 21.53 36.67 21.29Q36.76 21.05 36.77 20.79Q36.78 20.49 36.68 20.25Q36.58 20.01 36.35 19.86Q36.12 19.72 35.72 19.72ZM41.09 20.12Q41.05 20.1 40.98 20.09Q40.91 20.07 40.79 20.07Q40.42 20.07 40.05 20.27Q39.69 20.46 39.33 20.88Q38.97 21.29 38.59 21.94L38.33 21.82Q38.78 20.81 39.25 20.25Q39.72 19.69 40.22 19.47Q40.72 19.25 41.24 19.25Q41.41 19.25 41.58 19.26Q41.76 19.28 41.91 19.32Q42.06 19.35 42.17 19.39L40.96 23.31H40.87Q41.49 22.01 42.15 21.1Q42.82 20.19 43.5 19.7Q44.18 19.22 44.82 19.22Q45.27 19.22 45.48 19.43Q45.69 19.64 45.69 19.97Q45.69 20.21 45.58 20.39Q45.47 20.56 45.29 20.67Q45.11 20.77 44.9 20.77Q44.82 20.77 44.73 20.7Q44.64 20.62 44.52 20.49Q44.42 20.35 44.29 20.26Q44.15 20.17 43.99 20.17Q43.71 20.17 43.35 20.42Q42.99 20.68 42.6 21.13Q42.21 21.59 41.82 22.19Q41.43 22.8 41.1 23.52Q40.77 24.23 40.53 25L39.62 28H38.7Z"

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
    # «Cyber»: tracciati, non testo (JUDY, 07/10: il corsivo di sistema cambiava da un computer
    # all'altro e Iowan ha licenza Monotype). È CYBER_PATH, qui sotto: stessa altezza, stessa linea.
    # alzato di 3,3: la coda della «y» di Newsreader scende fino a 33,28 e Boomer comincia a 32;
    # così il punto più basso sta a 29,98, 2 unità sopra Boomer (JUDY, 07/10)
    cyber = f'<path class="wm-cyber" fill="{CARTA}" transform="translate(0,-3.3)" d="{CYBER_PATH}"/>'
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
