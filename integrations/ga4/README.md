# Google Analytics 4 (GA4) integration

Henter rapport-data (sessioner, brugere, konverteringer m.m.) fra en GA4-property via Google Analytics Data API.

## 1. Forudsætninger

- Adgang til den GA4-property, I vil hente data fra (find dit **Property ID** under GA4 → Admin → Property Settings, et tal a la `123456789`).
- En Google Cloud-konto (gratis) til at oprette et projekt og en service account.

## 2. Opret en service account (engangsopsætning)

1. Gå til [Google Cloud Console](https://console.cloud.google.com/) og opret et nyt projekt (eller genbrug et eksisterende).
2. Aktivér **Google Analytics Data API** for projektet: API'er & tjenester → Aktivér API'er → søg "Google Analytics Data API" → Aktivér.
3. Opret en service account: IAM & Admin → Service Accounts → Create Service Account. Giv den et navn, fx `ga4-reporting`.
4. Opret en nøgle til service accounten: fanen Keys → Add Key → Create new key → JSON. Gem den downloadede fil som `integrations/ga4/service-account.json` (den er allerede i `.gitignore`, så den ikke committes).
5. Kopiér service accountens e-mail (ser ud som `ga4-reporting@dit-projekt.iam.gserviceaccount.com`).
6. Gå til GA4 → Admin → Property Access Management → tilføj service account-e-mailen som **Viewer**.

## 3. Installer afhængigheder

```bash
cd integrations/ga4
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Konfigurér

```bash
cp .env.example .env
```

Udfyld i `.env`:
- `GA4_PROPERTY_ID` — property-ID'et fra trin 1
- `GA4_SERVICE_ACCOUNT_FILE` — sti til JSON-nøglen (default: `service-account.json`)

## 5. Kør en rapport

```bash
python ga4_report.py --start-date 30daysAgo --end-date today
```

Output er en tabel med dato, sessioner, brugere og konverteringer. Se `ga4_report.py` for at tilpasse dimensioner/metrics.
