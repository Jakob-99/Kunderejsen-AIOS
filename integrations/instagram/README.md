# Instagram-opslag integration

Publicerer billed-/video-opslag på en Instagram Business-konto via Meta Graph API (Content Publishing).

**Vigtigt:** Instagram-postering kræver, at billedet/videoen ligger på en **offentligt tilgængelig URL** — Meta's API henter selv filen derfra, du kan ikke uploade en lokal fil direkte.

## 1. Forudsætninger

- En **Instagram Business- eller Creator-konto**, koblet til en **Facebook-side** I administrerer.
- En Facebook-konto med admin-adgang til siden.

## 2. Opret Meta-app og hent adgang (engangsopsætning)

1. Gå til [Meta for Developers](https://developers.facebook.com/apps/) → **Create App** → vælg type "Business".
2. Tilføj produktet **Instagram Graph API** til appen (App Dashboard → Add Product).
3. Sørg for at Instagram-kontoen er en Business/Creator-konto og er koblet til en Facebook-side (Instagram-appen → Indstillinger → Konto → Skift til professionel konto, hvis nødvendigt).
4. Brug [Graph API Explorer](https://developers.facebook.com/tools/explorer/) til at:
   - Vælge din app
   - Generere et **User Access Token** med permissions: `instagram_basic`, `instagram_content_publish`, `pages_read_engagement`, `pages_show_list`
   - Kalde `GET /me/accounts` for at finde din **Page ID**
   - Kalde `GET /{page-id}?fields=instagram_business_account` for at finde dit **Instagram Business Account ID** (`IG_USER_ID`)
5. Konvertér user-tokenet til et **langlivet token** (60 dage):
   ```
   GET /oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token}
   ```
   Tokenet skal fornyes inden det udløber — for produktionsbrug bør I sætte en påmindelse eller automatisere fornyelsen.
6. For at appen kan publicere uden Meta's app-review, skal appen enten være i **Development mode** med jeres egen konto tilføjet som testbruger, eller have gennemført **App Review** for `instagram_content_publish` til produktion for andre konti.

## 3. Installer afhængigheder

```bash
cd integrations/instagram
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Konfigurér

```bash
cp .env.example .env
```

Udfyld i `.env`:
- `IG_USER_ID` — Instagram Business Account ID fra trin 2
- `IG_ACCESS_TOKEN` — det langlivede access token fra trin 2

## 5. Post et billede

```bash
python instagram_post.py --image-url "https://example.com/mit-billede.jpg" --caption "Ny figur klar til afhentning! 🎁"
```

Scriptet opretter en media-container og publicerer den derefter — Instagram kan tage nogle sekunder om at behandle billedet, så scriptet venter og tjekker status før publicering.
