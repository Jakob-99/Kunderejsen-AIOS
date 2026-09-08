# Templates

Skabeloner til gentaget markedsførings- og salgsmateriale (fx sociale opslag, annoncer, produktkort) — så nye stykker indhold kan laves hurtigt og konsistent i Figurio Sage-stilen, i stedet for at starte forfra hver gang.

## Filer

- `annonce-tilbud.html` — annonceskabelon (1080×1080, til Instagram/Facebook) i AG1-inspireret "bundle-tilbud"-stil: overskrift, spar-badge, 2-3 produkter side om side med streget/gratis-priser, CTA-knap, småprint. Bygget i Figurio Sage-designsystemet (se `figurio-sage-design`-skillet).
- `annonce-tilbud-preview.png` — renderet eksempel af ovenstående.

## Sådan genbruges annonce-tilbud.html

Åbn filen i browser eller ret direkte i koden:

1. Skift overskrift, subline og badge-tekst (`.headline`, `.save-badge`)
2. Skift billeder — peg `src` på andre filer i `../product-shots/`
3. Skift priser/labels under hvert billede
4. Skift CTA-tekst og småprint nederst

Til at generere et PNG fra HTML'en (fx til at dele/preview), brug Playwright/headless Chromium til at tage et 1080×1080 screenshot af filen.
